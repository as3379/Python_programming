"""Write the test data for the function: int getSmallestIntegerPosition(int[] A) (smallest_sofar)

This method accepts as input integer array that is already sorted and rotated "n" number of items where n is less than the size of the array
For Example: The test data can be {4,5,6,1} This was derived from {1, 4, 5,6} afer sorting and rotating the array for 3 times
And output of the function returns the index of integer that has the smallest value

Eg: {4,5,6,1}: the smallest value is 1 and its index is 3


"""

def smallest_integer_index(A):

    small_sofar = A[0]
    index = 0
    n = len(A)
    for i in range(1, n):
        if A[i] < small_sofar:
            small_sofar = A[i]
            index = i
        else:
            continue
    print(small_sofar)
    print(index)

smallest_integer_index([4,5,6,1])