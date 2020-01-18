
"""find two elements of an int array that add to a sum."""
A = [1, 4, 45, 6, 10, 8]
n = len(A)
sum = 16
s = []
for i in range(0, n):
        temp = sum-int(A[i])
        if (temp in A):
            s.append(temp)
            s.append(A[i])
            break
s = set(s)
print (s)
