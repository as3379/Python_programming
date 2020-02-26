"""FIBONNOCCI - a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, etc.

OR Amazon - Staircase problem"""

# 0, 1, 1, 2, 3, 5, ...
n = int(input('Enter the number: '))
a = 0
b = 1
FIB_ARRAY =[0, 1]

#create fibnocci series/ Array
for i in range (2, 10):
    fib =  a + b
    FIB_ARRAY.append(fib)
    a = b
    b = fib

print(FIB_ARRAY)

#check whether the given number is in that array
if n in FIB_ARRAY:
    print(n, 'is a fibonocci number')
else:
    print(n ,'is not a fibonocci number')
