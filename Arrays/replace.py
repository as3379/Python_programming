def string_replace(s,a):
    S =[]
    A =[]

    #To remove numbers and returnn characters

    for i in s:
        if i.isalpha():
            S.append(i)
    print(S)
    print(''.join(S))


    #To remove numbers and returnn characters

    for i in a:
        if i.isdigit():
            A.append(i)
    print(A)
    print(''.join(A))

string_replace(s='ashi13', a='ashi13')
