"""Input : ab50dt60h4q, Output: Sum of integers i.e. 50+60+4= 114
"""
a = "ab500dt60h40q"
s = []
sum = 0
for i in a:
  if i.isdigit():
      s.append(int(i))

  else:

      n = len(s)
      for i in range(0, n):
          sum += s[i]*(10**(n-i-1))
      s = []

print("Sum of integers from given string: ", sum)






