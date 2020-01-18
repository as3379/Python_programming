#Method1 - Iterator

n = input('Enter series of values seperated by space: ')
a = n.split(" ")
l = len (a)
b = []

for i in range (0, l):
    if a[i] not in b:
        b.append(a[i])
    else:
        continue
print(b) #  list without duplicates


#Method2 - remove duplicates using set() and display duplcates

c = set(a)
print(c)
d = {}
duplicates = []

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print (d)

for k in d:
    if d[k] > 1:
        duplicates.append(k)

print(duplicates)
