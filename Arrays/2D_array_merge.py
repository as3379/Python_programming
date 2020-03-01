"""Merge two dimesional Array
Consider array1 ={{10, 15}, {30, 50}}
array2 ={{20,40}, {5, 10}}
Merged array should be sandwitched (array 1 should be sandwitched with array 2) 2w1w if value range is less than the previously added value then that value should not be added to the merged array
Output should be {10, 20, 30, 40, 50} --> 15, 5 and 10 should not be added
"""


def array_merge():
    a =[[10, 15], [30, 50]]
    b =[[20,40], [5, 10]]
    n = len(a)
    c = []

    for i in range(0, n):
        c.append(a[i][0])
        for j in range(0,n):

            if c[-1] < a[i][j]:
                c.append(a[i][j])
            if c[-1] < b[i][j]:
                c.append(b[i][j])
    c = sorted(c)
    print(c)


array_merge()
