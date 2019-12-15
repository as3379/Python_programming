"""1. write a program to remove duplicates numbers from the list and display the duplicates ? OR
2. Given an array of integers, how would you move the duplicate integers into a different array?
What is the efficiency of your algorithm?  OR
3.Find the unique numbers in an integer array"""

n = input('Enter series of values seperated by space: ')
a = n.split(" ")
l = len (a)
b = []
c[]
for i in range (0, l):
    if a[i] not in b:
        b.append(a[i])
    else:
        continue
print(b) #  list without duplicates
