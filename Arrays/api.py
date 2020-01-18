def run_api(jobgroup_id, test_id, **kwargs):
    """
    read the config to find the required args and run the API test
    """
    config = JobConfig.query.filter((JobConfig.test_id == test_id), (JobConfig.end_date == None)).first()
    if config:
        args = config.__dict__
        logger.info('Submitting test_id:%s', args.get('test_id'))
        test_name = args.get('test_name')
        env = args.get('website')
        user = args.get('user')
        password = args.get('password')
        args = {i: args[i] for i in args if i not in ['end_date', 'modified_timestamp', '_sa_instance_state', 'email',
                                                      'test_id']}
        args['jobgroup_id'] = jobgroup_id
        # Arguments that can be updated via run_deploy_api_post POST method
        logger.info("IN RUN_API METHOD")
        logger.info("KWARGS BELOW")
        logger.info(', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]))
        if 'version' in kwargs:
            args['platform'] = kwargs['version']
        if 'verbosity' in kwargs:
            args['browser_version'] = kwargs['verbosity']
        if 'test' in kwargs:
            args['browser_name'] = kwargs['test']
        version = args.get('platform')
        verbosity = args.get('browser_version')
        tests = args.get('browser_name')
        importlib.invalidate_caches()

    # Construct the finalized API endpoint.
    env = cfg.DEF_ENV.get(env, 'https://' + env + '/')
    env = env + version + '/gw.k'
    os.environ['reg_test_endpoint'] = env  # set API endpoint as env var
    if verbosity is not None:
        verbosity = int(verbosity)
    else:
        verbosity = 2
    if tests is not None:
        logger.info("CONSTRUCTING TEST SUITE")
        tests_to_run = list(OrderedDict.fromkeys(['py_tests.' + test for test in tests]))
        for test in tests_to_run:
            if test not in cfg.TEST_MODULES:
                logger.info("Error: no test named: " + test)
    # --------------------------- TEST INITIALIZATION ---------------------------
    job_log = JobLogs()
    job_log.jobgroup_id = jobgroup_id
    db.session.add(job_log)
    db.session.commit()
    job_log.status = 1
    db.session.commit()
    start_time = datetime.datetime.today()
    logger.info('Starting Test Suite on %s' % env)
    logger.info('Creating session ...')
    # Log in and create/validate the session.
    response = api.log_in(user, password)
    if response['rc'] != '0':
        logger.critical('fail\nLogin error with rc: %s'  %response['rc'])
        logger.critical('msg: %s' %response['msg'])
    session = api.create_session(user, response)
    logger.info('API Session created successfully\n')
    # Set relevant OS environ variables for use in unit tests.
    os.environ['reg_test_unecryp_pswd'] = password
    utils.set_env_vars(user, session)
    # Get dbmv info (to skip tests...).
    response = api.post('getuser', session)
    user = response['user']
    if user['dbmv'] == '': user['dbmv'] = b'0'
    os.environ['reg_test_dbmv'] = str(int(float(user['dbmv'])))
    # ------------------------------- TEST RUNNER -------------------------------
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=verbosity,resultclass=TextTestResultWithSuccesses)
    suite = unittest.TestSuite()
    # Validate the requisite dependencies' existence.
    logger.info('Validating table/directory dependencies on 1010.\n')
    checker = unittest.TestSuite()
    checker.addTest(loader.loadTestsFromName('py_tests.000_setup_checker'))
    res = unittest.TextTestRunner().run(checker)
    if not res.wasSuccessful():
        logger.info('\nTable and directory dependencies were not set properly.')
    logger.info('\n\nExecuting test suite.\n')
    # Organize test suite depending on tests selected.
    # Default value is None to run all tests unless specified otherwise
    if tests is None:
        for test in tests_to_run:
            suite.addTest(loader.loadTestsFromName(test))
    else:
        tests = cfg.TEST_MODULES
        for test in tests:
            suite.addTest(loader.loadTestsFromName(test))
    suite.addTest(loader.loadTestsFromName('py_tests.zzz_logout000'))
    suite_results = runner.run(suite)
    utils.clear_env_vars(session)
    # ----------------------------- RESULT HANDLING -----------------------------
    time_taken = (datetime.datetime.now() - start_time).total_seconds()
    time_taken_minutes = str(datetime.timedelta(seconds=time_taken))
    ret_val = int(not suite_results.wasSuccessful())
    # Construct the JSON return.
    # results is a dictionary representing the JSON tree structure.
    # json_results is the dictionary in JSON string format, ready for immediate use.
    # With a webclient, we probably just want to return the `json_results` variable.
    results = utils.get_json(suite_results)
    json_results = json.dumps(results)
    # Slack integration -- if -s flag is set, then send message to appropriate channel.
    headers = {
        0: ":heavy_exclamation_mark: *%s* FAILED" % test_name,
        1: ":white_check_mark: *%s* PASSED" % test_name,
    }
    channels = {
        0: 'CLWFNLYNL',  # python-api-failures
        1: 'CLW1YFS76',  # python-api-successes
    }
    job_log.jobgroup_id = jobgroup_id
    slack_token = "xoxp-4064541615-710088119681-790147809920-6e8e263b8d7d7d2bd492497d0ab0c92e"  # ~uwu~
    client = SlackClient(token=slack_token)
    is_successful = suite_results.wasSuccessful()
    channel = channels[is_successful]

    header = headers[is_successful]

    if is_successful:
        job_log.status = 0
        db.session.commit()
        body = "*Test started at* {time}\n*Test Duration:* {duration} \n*{num}* tests ran. " \
            .format(time=str(start_time), duration=time_taken_minutes, num=suite_results.testsRun)
    if not is_successful:
        job_log.status = -1
        db.session.commit()
        body = '*{num1}* tests ran. *{num2}* tests failed.\nSee thread for verbose test failures.' \
            .format(num1=suite_results.testsRun, num2=len(suite_results.failures))

    message = header + "\n\n *Test Name:* " + test + "\n*Test run at* " + env + " \n" + body

    try:
        response = client.api_call("chat.postMessage", channel=channel, text=message,)
    except:
        logger.critical("Error sending message via Slack")
    try:
        if not is_successful:
            ts = response['ts']
            text = 'Copy into https://codebeautify.org/jsonviewer.'
            client.api_call ("chat.postMessage", channel=channel, thread_ts=ts, text=text,)
            if json_results is not None:
                client.api_call ("chat.postMessage", channel=channel, thread_ts=ts, text='```' + json_results + '```',)
    except:
        logger.critical("Error sending message via Slack")
