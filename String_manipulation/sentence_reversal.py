
n = input ('Enter the series in space seperated form: ')
a = n.split(" ")
a = list(a)
print(a)
b = []

# if there are spaces preceding or following the sentence
for i in a:
    if i is not '':
        b.append(i)
print(b)

l = len(b)
n = int (l/2)

for i in range (0, n):
    temp = b[i]
    b [i] = b[l-1]
    b[l-1] = temp
    l = l-1
print (b)

print(" ".join(b))
