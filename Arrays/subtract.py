"""Given an array with numbers 1-5, how would you subtract
one number from each index?"""
def subtract (a):

    n = len(a)

    for i in range (0, n):
        a[i] = a[i]-1
    print(a)

subtract(a=[1,2,3,4,5])

"""Given an array with numbers 1-5, how would you
subtract one number from every EVEN number in each index?"""

def subtract_even (a):

    n = len(a)

    for i in range (0, n):
        if a[i]%2 ==0:
            a[i] = a[i]-1
    print(a)

subtract_even(a=[1,2,3,4,5])

#Subtract 1 from even indexes:

def subtract_even_index (a):

    n = len(a)

    for i in range (0, n):

        if i%2 ==0:
            a[i] = a[i]-1
    print(a)

subtract_even_index(a=[1,2,3,4,5])
