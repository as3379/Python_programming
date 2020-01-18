def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

print(list(accumu([10, 20, 30, 40, 50])))
