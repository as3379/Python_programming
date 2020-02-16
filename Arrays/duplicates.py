#Method1 - Iterator
#
# n = input('Enter series of values seperated by space: ')
# a = n.split(" ")
a = [2, 3,3, 4, 5, 6, 3]
l = len (a)
b = []

for i in range (0, l):
    if a[i] not in b:
        b.append(a[i])
    else:
        continue
print("List without duplicates using Iterator: %s" %b) #  list without duplicates


#Method2 - remove duplicates using set() and display duplcates

c = set(a)
print("List without duplicates using set(): %s" %c)
d = {}
duplicates = []

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

for k in d:
    if d[k] > 1:
        duplicates.append(k)

print(duplicates)
