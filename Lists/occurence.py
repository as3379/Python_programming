"""write a program where there are multiple users logging
into the system or file and I want to know the login Occurrences
of the each user . Note : The file is separated by the commas.
ex: User1 , User2, user1 , user3.........  
"""
n = input ('Enter the series in space seperated form: ').split(" ")
a = list(n)
l = len(a)
x = input ('Enter the value to check occurence: ')
count = 0
for i in a:
    if x == i:
        count = count+1
print (count)
