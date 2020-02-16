"Find Array pairs for given Sum."

def printPairs(arr, arr_size, sum):

    # Create an empty hash set
    s = set()
    l = []

    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in s):

            x = list((str(arr[i]),str(temp)))
            l.append(x)
        s.add(arr[i])


    print(l)

# driver program to check the above function
A = [1, 4, 45, 6, 10, 8, 8, 12]
n = 16
printPairs(A, len(A), n)
