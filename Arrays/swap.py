a = input("Enter series of values separated by space: ")
b = a.split(" ")
n = len(b)
temp = b[0]

# to swap first and last positions
b[0] = b[n-1]
b[n-1] = temp

print (b)

#to swap two given positions
temp = b[0]
b[0] = b[2]
b[2]= temp
print (b)
