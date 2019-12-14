n = input('Enter series of numbers seperated by sapce: ')
a = n.split(" ")
l = len(a)
flag = 0
for i in range (0, l-1):
    if a[i] <= a[i+1]:
        flag = 1
print(flag)

if flag ==0:
    print("Array is not monotonic")
else:
    print("Array is monotonic")
