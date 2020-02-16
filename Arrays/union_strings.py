"""
Find the union of two strings?
"""
import collections
#Method 1 - Using set()


a = 'once up on time'
b = 'time is money'

#
# A = a.split(" ")
# B = b.split( " ")
# C = A + B
# C = OrderedSet(C)
#
# D = ' '.join(C)
# print (D)


#Method 1

def union1():
    a = 'once up on time'
    b = 'time is money'

    a = a.split(" ")
    b = b.split(" ")
    A = []
    B = []

    #Make a list without using list()

    for i in a:
        A.append(i)


    for i in b:
        B.append(i)


    for i in A:
        if i in B:
            B.remove(i)

    C = A + B

    D = ' '.join(C)
    print(D)

#Method 3 - using set() for individual ones

def union2(a,b):

    a = list(a)
    b = list(b)

    c = a + b
    c = set(c)
    print(c)




union1()
union2(a='ashi', b='gowda')

