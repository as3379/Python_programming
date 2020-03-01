"""Flip two dimensional array"""

#Method1: Iterator and zipping
def twoD_reverse(arr):
    n = len(arr)
    b = []

    for i in range(0, n):
        b.append(arr.pop())
    flip = zip(*b)
    return list(flip)

print(twoD_reverse([ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]))

#Method2: Slicing and Zipping
def flip(arr):
    rev_arry = arr[::-1]
    flip = zip(*rev_arry)
    return list(flip)

print(flip([ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]))

#Method3: Uisng numpy

import numpy as np

arr = np.array([ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ])

arr = np.flip(arr, axis = 0)
arr = arr[::-1]
print(arr)