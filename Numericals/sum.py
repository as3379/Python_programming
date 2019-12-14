#Sum of first N squares
n = int (input('Enter the number: '))
square_sum = 0
cube_sum = 0
for i in range(0,n+1):
    square_sum += i*i
    cube_sum += i*i*i
print ('Sum squares of first N numbers is' , square_sum)
print ('Sum cubes of first N numbers is' , cube_sum)
