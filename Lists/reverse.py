"""Determine if a string is a palindrome/ Reverse a string  """
n = input ('Enter the series in space seperated form: ')
n1 = n.split(" ")
a = list(n1)
print(a)

l = len(a)
n = int (l/2)


for i in range (0, n):
    temp = a[i]
    a [i] = a [l-1]
    a[l-1] = temp
    l = l-1
print (a)
