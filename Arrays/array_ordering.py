a = input('Enter the series of comma seperated number:  ')
b = a.split(" ")
l = len(b)
max = b[0]
for i in range (0, l):
    if b[i] > max:
        max = b[i]
print (max)
