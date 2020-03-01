"""Search an element in array without using linear search technique - Binary search
"""

def binary_search(a, x):
    l = len(a)
    m = l//2

    r = 0
    if a[m] == x:
        return m
    else:
         if x < m:
             for i in range(r, m):
                 if a[i] == x:
                     return i, "found"
         else:
             r = m

             for i in range (r,l ):
                 if a[i] == x:
                     return i, "found"
    return -1

print(binary_search([ 2, 3, 4, 10, 40 ] , 40))


