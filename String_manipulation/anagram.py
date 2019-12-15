"""how to tell if two strings are anagram"""

A = "listen"
a = A.lower()
a=list(a)
B = "silent"
b = B.lower()
b=b.lower()
b=list(b)
a = a.sort()
b = b.sort()
if a == b:
    print('Strings are anagram')
else:
    print('Strings are not anagram')
