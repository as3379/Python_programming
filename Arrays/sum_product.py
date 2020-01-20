n = input('Enter numbers: ').split(" ")
a = list(n)
n = len (a)
sum = 0
multiple =1
for i in range (0, n):
    sum += int(a[i])
    multiple *= int(a[i])
print(sum)
print(multiple)
