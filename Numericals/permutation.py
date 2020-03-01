#Method1: Using swapping and Iterator
def permutation(s, l =0):
    a = list(s)
    r = len(a)
    if l ==r :
        print("".join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permutation(a, l+1)
permutation("123")

#Method2: Using itertools
from itertools import permutations
print ([''.join(p) for p in permutations('123')])
