"""Optimal Program to find greatest number in an integer array without sorting  (max_sofar)"""


def greatest(a):

    max_sofar = a[0]
    n = len(a)

    for i in range (1, n):
        if a[i] > max_sofar:
            max_sofar = a[i]
        else:
            continue
    print (max_sofar)


greatest([2, 3, 3, 9, 5, 3, 4, 1, 7])