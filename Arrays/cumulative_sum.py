def cum_sum(lis):
    total = 0
    for x in lis:
        total += x
        yield total


print(list(cum_sum([10, 20, 30, 40, 50])))
