# Not working

def sort(a):

    n = len(a)

    for i in range (0, n-1):

        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
        else:
            continue
    print(a)


sort(a=[3,1,3,4,5,2])
