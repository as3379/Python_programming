def printPairs(arr, arr_size, sum):

    # Create an empty hash set
    s = set()
    l = []

    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):

            x = list((str(arr[i]),str(temp)))
            print(x)
            l.append(x)
        print(l)
        s.add(arr[i])

# driver program to check the above function
A = [1, 4, 45, 6, 10, 8, 8, 12]
n = 16
printPairs(A, len(A), n)
