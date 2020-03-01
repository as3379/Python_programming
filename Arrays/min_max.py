"""Find min and max for given array.
"""
def min_max(a):
    min = max = 0
    n = len (a)
    if a[0] > a[1]:
        min = a[1]
        max = a[0]
    else:
        min = a[0]
        max = a[1]
    for i in range (2, n):
        if a[i]<= min:
            min = a[i]
        elif a[i]>= max:
            max = a[i]
    print(min , max)
# Driver code
a = [5, 4, 5, 6, 5, 4, 3,9, 2, 0, -9]
min_max(a)