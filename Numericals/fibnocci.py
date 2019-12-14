#FIBONNOCCI
# 0, 1, 1, 2, 3, 5, ...
n = int(input('Enter the number: '))
a = 0
b = 1
FIB_ARRAY =[0, 1]
#create fibnocci series/ Array
for i in range (1, 10):
    fib =  a + b
    a=b
    b=fib
    FIB_ARRAY.append(fib)

#check whether the given number is in that array
if n in FIB_ARRAY:
    print(n, 'is a fibonocci number')
else:
    print(n ,'is not a fibonocci number')
