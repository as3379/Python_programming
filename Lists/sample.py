"""Given an array with numbers 1-5, how would you subtract
one number from each index?"""

x = int (input('Enter number by space seperated format: ')).strip(" ")
a = list(x)
n = len (a)
for i in range (0, n):
    a[i] = a[i] -1
print(a)
