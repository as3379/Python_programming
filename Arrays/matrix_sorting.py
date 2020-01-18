# Python 3 implementation to
# sort the matrix row-wise
# and column-wise
MAX_SIZE = 10

# function to sort each
# row of the matrix
def sortByRow(mat, n):
    for i in range (n):

        # sorting row number 'i'
        for j in range(n-1):
            if mat[i][j] > mat[i][j + 1]:
                temp = mat[i][j]
                mat[i][j] = mat[i][j + 1]
                mat[i][j + 1] = temp

# function to find
# transpose of the matrix
def transpose(mat, n):
    for i in range (n):
        for j in range(i + 1, n):

            # swapping element at
            # index (i, j) by element
            # at index (j, i)
            t = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = t

# function to sort
# the matrix row-wise
# and column-wise
def sortMatRowAndColWise(mat, n):

    # sort rows of mat[][]
    sortByRow(mat, n)

    # get transpose of mat[][]
    transpose(mat, n)

    # again sort rows of mat[][]
    sortByRow(mat, n)

    # again get transpose of mat[][]
    transpose(mat, n)

# function to print the matrix
def printMat(mat, n):
    for i in range(n):
        for j in range(n):
            print(str(mat[i][j] ), end = " ")
        print();

# Driver Code
mat = [[ 4, 1, 3 ],
       [ 9, 6, 8 ],
       [ 5, 2, 7 ]]
n = 3

print("Original Matrix:")
printMat(mat, n)

sortMatRowAndColWise(mat, n)

print("\nMatrix After Sorting:")
printMat(mat, n)

#Time Complexity: O(n2log2n).
