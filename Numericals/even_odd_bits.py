"""implement a function that takes an integer and
returns whether or not the number had an odd or even number of 1 bits."""

def bits(n):
    x = f'{n:08b}'
    l = len(x)
    print(x, l)
    d = {}
    for i in x:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    print(d)

    if d['1']%2 == 0:
        print("Integer has even number of 1 bits")
    else:
        print("Integer has odd number of 1 bits")


bits(23)
bits(37)