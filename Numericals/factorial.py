n = int (input('Enter the number: '))
fact = 1

if n ==0:
    print(1)
else:

    for i in range (0, n):
        fact = fact*(n-i)
print(fact)


#Method2 - Using Recursion

def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)


print(factorial(0))