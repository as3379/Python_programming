start = 11
end = 25

for val in range(0, 10):

   # If num is divisible by any number
   # between 2 and val, it is not prime
   # if val > 1:
       for n in range(2, val):
           if (val % n) == 0:
               break
       else:
           print(val)


   # If num is divisible by any number
   # between 2 and val, it is not prime



# n = int (input('Enter the number: '))
# for i in range (2, n):
#     if (n%i==0):
#         print("Number is not prime")
#     else:
#         print("Number is prime")
#     break





#even or odd

# number = int (input('enter the number: '))
# if number%2 ==0:
#     print(number, "is a even number")
#
# else:
#     print(number, "is a odd  number")
