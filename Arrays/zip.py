x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
z = zip(y, x)
print(z)
s = [i for _, i in z]
print(s)
