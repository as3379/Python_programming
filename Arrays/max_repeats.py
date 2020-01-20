"""finding the element that's repeated a maximum times in a set of array"""
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

# Method2:
def mostFrequent(arr, n):

    # Insert all elements in Hash.
    d = {}
    for i in a:
        if i not in d:
            d[i] =1
        else:
            d[i] +=1

    # find the max frequency
    max_count = 0
     #important
    for i in d:
        if (max_count < d[i]):
            res = i
            max_count = d[i]

    return res

# Driver Code
a =[2, 3, 3, 5, 3, 4, 3,1, 7]
n = len(arr)
print(mostFrequent(arr, n))

# Method3
a=[2, 3, 3, 5, 3, 4, 1, 7]
a_dict={}
for i in a:
    if i not in a_dict:
        a_dict[i] =1
    else:
        a_dict[i] +=1
print(a_dict)
print(sorted(a_dict.items(), key = lambda kv:(kv[1], kv[0])))
print(max(a_dict, key=a_dict.get) )
