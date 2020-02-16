# Subtract 1 from each element

def subtract (a):

    n = len(a)

    for i in range (0, n):
        a[i] = a[i]-1
    print(a)

subtract(a=[1,2,3,4,5])

#Subtract 1 from each even elements

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

    for i in range (1, n):

        if i%2 ==0:
            a[i] = a[i]-1
    print(a)

subtract_even_index(a=[1,2,3,4,5])
