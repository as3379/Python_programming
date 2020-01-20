a = "AAAAaabbbccccaaa"
new_string = ""

count = 1
for i in range(len(a)-1):
  if a[i] == a[i+1]:
    count += 1
  else:
    new_string += a[i]+ str(count)
    count = 1
new_string += a[i]+ str(count)
print (new_string)
