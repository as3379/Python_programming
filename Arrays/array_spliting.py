b = [2, 5, 6, 8, 4, 9]
temp = b.copy()
k =3

for i in range (0, k):
    b.pop(0)
    b.append(temp[i])

print(b)
