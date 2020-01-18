a = 'ashritha'
b = list(a)
print(b)
c = []
s = {}
for i in b:
    if i not in c:
        c.append(i)
        s[i] = 1
    else:
        s[i] += 1
print (s)
for i in s:
    if s[i] == 1:
        print("first non - repetitive number", i)
        break
