a = input('Enter the series of comma seperated number:  ')
b = a.split(" ")
print (b)
sum = 0
for i in b:
    sum += int(i)

print (sum)
