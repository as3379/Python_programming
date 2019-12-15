def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        j = i + 1
        for j in range(j, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]

l = len(list1)
print (Repeat(list1))

#method2
newlist = [t for t in set(list1) if list1.count(t) > 1]
print(newlist)
