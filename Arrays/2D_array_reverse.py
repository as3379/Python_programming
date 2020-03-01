#Method1: Iteractor
def twoD_reverse(arr):
    n = len(arr)
    b = []

    for i in range (0, n):
        b.append(arr.pop())
    print(b)



twoD_reverse([ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ])

#Method2: Slicing

def slicing(arr):
    rev_arry = arr[::-1]
    print(rev_arry)


slicing([[1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]])