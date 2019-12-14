n = input ('Enter the series in space seperated form: ').split(" ")
a = list(n)
l = len(a)
x = input ('Enter the value to check occurence: ')
count = 0
for i in a:
    if x == i:
        count = count+1
print (count)
