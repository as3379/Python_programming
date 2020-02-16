"Find the maximum element in a given array"
b = [575,6,2,39,10, 510]
l = len(b)
max = b[0]
for i in range (0, l):
    if b[i] > max:
        max = b[i]
print (max)
