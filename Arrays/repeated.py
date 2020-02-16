# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]

#Method1:

d = {}
duplicates = []
for i in list1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for k in d:
    if d[k] > 1:
        duplicates.append(k)

print("Finding repeats using dictionary: ", duplicates)


# Method2
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        j = i + 1
        for j in range(j, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


l = len(list1)
print("Finding repeats using Iterator: " , Repeat(list1))

#Method3
newlist = [t for t in set(list1) if list1.count(t) > 1]
print("Finding repeats using compression: ", newlist)




