a = "AAAAaabbbccccaaa"

start, end = 0, 1
new_string = a[0]
count = 1
while end < len(a):
  if a[start] == a[end]:
    count += 1
    end += 1
  else:
    new_string += str(count)
    start, end = end, end+1
    new_string += a[start]
    count = 1
new_string += str(count)
print (new_string)
