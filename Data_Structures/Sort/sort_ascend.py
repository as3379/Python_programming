# Not working

n = input('Enter numbers: ').split(" ")
a = list(n)
n = len (a)
for i in range(0,n-1):
    if a[i]>= a[i+1]:
        a[i+1] = a[i]
        i+=1
print(a)
