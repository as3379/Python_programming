

def finder1(arr1, arr2):

    count = {}

    for i in arr1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    for j in arr2:
        if j in count:
            count[j] -= 1
        else:
            count[j] =1
    print(count)

    for k in count:
        if count[k] > 0:
            print(k)



arr1 = [4,4,4, 5, 5]
arr2 = [4, 4, 5,5 ]

#1, 0, 4
#finder1(arr1, arr2)


#Find the missing element in an array of range
"""For an array of size n,
there are numbers from i to i + n in it with one missing number.
Design algorithm finding the missing number."""

def finder2 (arr):
    n = len(arr)

    for i in range (n+1):
        if i in arr:
            continue
        else:
            print(i)
finder2(arr=[1, 2, 4, 5, 6])
