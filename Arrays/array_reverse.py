"Reverse given Array"

b = [2, 5, 6, 8, 4, 9]
a = []
k = 3

for i in range (0, len(b)):
    s = b.pop(-1)
    a.append(s)
print(a)
