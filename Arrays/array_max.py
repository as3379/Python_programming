# a = input('Enter the series of comma seperated number:  ')
# b = a.split(" ")

"""Find the highest element of the given Array"""
b = [5,6,2,39,10, 510]
l = len(b)
max = b[0]
for i in range (0, l):
    if b[i] > max:
        max = b[i]
print (max)
