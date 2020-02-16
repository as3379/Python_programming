b = [2, 5, 6, 8, 4, 9]
k = 3

for i in range (0, k):
    s = b.pop(0)
    b.append(s)

print(b)
