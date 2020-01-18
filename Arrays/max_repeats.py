def maxRepeating(arr, n,  k):

    # Iterate though input array, for every element
    # arr[i], increment arr[arr[i]%k] by k
    for i in range(0,  n):
        arr[arr[i]%k] += k

    # Find index of the maximum repeating element
    max = arr[0]
    result = 0
    for i in range(1, n):

        if arr[i] > max:
            max = arr[i]
            result = i

    # Uncomment this code to get the original array back
    #for i in range(0, n):
    #    arr[i] = arr[i]%k

    # Return index of the maximum element
    return result


# Driver program to test above function
arr = [2, 3, 3, 5, 3, 4, 1, 7]
n = len(arr)
k = 8
print("The maximum repeating number is",maxRepeating(arr, n, k)) 
