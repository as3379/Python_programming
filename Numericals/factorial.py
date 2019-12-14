n = int (input('Enter the number: '))
fact = 1
for i in range (0, n):
    fact = fact*(n-i)
print(fact)
