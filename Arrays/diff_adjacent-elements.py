"""Find the first occurance of a given number from the series which has the difference between
the adjacent elements as 1. For Example {1, 0, -1,-2,-1,0,1,2,3} Note: Do not use Linear Search
"""
def search(arr, n, x):
    # Searching x in arr[0..n-1]
    i = 0
    while (i <= n-1):
    # Checking if element is found.
        if (arr[i] == x):
            return i
            break
        # Else jumping to abs(arr[i]-x).
        else:
            i += abs(arr[i] - x)
    return -1
# Driver code
arr = [5, 4, 5, 6, 5, 4, 3, 2]
n = len(arr)
x = 6

print(search(arr, n, x))