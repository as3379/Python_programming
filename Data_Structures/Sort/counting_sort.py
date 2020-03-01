"""Count sort can only be used for sample range of positive integers"""


def count_sort(a):
    b = {}
    c = []


    #count the occurence and create an array

    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    print(b)

    for i in b:
        c.append(b[i])

    n = len(c)


    # Calculate te running sum
    for i in range(1, n):
        c[i] = c[i] + c[i-1]
    print(c)


    # shift the array to right by 1 element and initiate first element to zero

    for i in range(0,n-1):
        c[n-1-i] = c[n-2-i]
    c[0] = 0
    print(c)

    d = []
    
    for i in a:
        x = c.index(i)
        print(x)



count_sort([7, 3,3, 1, 2, 0])