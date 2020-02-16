# n = input('Enter numbers: ').split(" ")
# a = list(n)
a = [1, 2, 3, 4, 5]
n = len(a)

sum = 0
multiple =1
for i in range (0, n):
    sum += int(a[i])
    multiple *= int(a[i])
print(sum)
print(multiple)


# Method2 : Recursion

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)



print(factorial(5))