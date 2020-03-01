"""Search an element in array without using linear search technique - Jump search
"""
import math

def binary_search(a, x):

    n = len(a)
    m = int(math.sqrt(n))
    start = 0
    end = m

    if x == a[m]:
        print("Found %d at: %d ", x, m)

    else:
        if x < m:
            for i in range(start, end):
                if a[i] == x:
                        return ("Found %d at: %d ", x, i)
        elif x > m:

            start = m
            end += (m +1)
            for i in range(start, end):
                if a[i] == x:
                    return("Found %d at: %d ", x, i)
    return -1


print(binary_search([ 2, 3, 4, 10, 40, 67, 89, 99 ], 90))