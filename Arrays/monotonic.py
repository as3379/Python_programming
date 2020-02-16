"""An array is monotonic if and only if it is monotone increasing,
or monotone decreasing"""
def isMonotonic(A):

    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


print(isMonotonic([5, 5, 5, 5]))