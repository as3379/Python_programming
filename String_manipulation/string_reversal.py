#String reversal

#Method1 - Iterative list
s = 'ashritha'
s = list(s)
n = len(s)
l = int(n/2)

for i in range(0,l):
    temp = s[i]
    s[i] =s[n-1]
    s[n-1]=temp
    n -= 1

print(''.join(s))

# Method2 - Slicing
s='ashritha'
n = s [::-1]
print(n)


#Method3 - looping
x = "ashritha"
w = ""
for i in x:
    w = i + w
print(w)
