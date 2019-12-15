"""Given an array with numbers 1-5, how would you subtract
one number from each index?"""

x = input('Enter number by space seperated format: ')
a = x.split(" ")
n = len (a)
for i in range (0, n):
    a[i] = int (a[i]) -1
print(a)


"""Given an array with numbers 1-5, how would you
subtract one number from every EVEN number in each index?"""
a = [3, 4, 5, 6]
for i in range (0, n):
    if i%2==0:
        a[i] = int (a[i]) -1
print(a)
