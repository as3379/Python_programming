"""
Find the union of two strings?
"""
a = 'once up on time'
b = 'time is money'

A = a.split(" ")
B = b.split( " ")
C = A + B
C = set(C)
print (C)
D = ' '.join(C)
print (D)


#Method 1

def union1(a, b):
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

    print(A+B)

#Method 2 - using set()

def union2(a,b):

    a = list(a)
    b = list(b)

    c = a + b
    c = set(c)
    print(c)




union1(a='ashi', b='gowda')
union2(a='ashi', b='gowda')
