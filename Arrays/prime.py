#Number is prime or not

num = 11

#Edge case

if num == 0 or num ==1:
    print(num, 'is not a prime Number')
else:
    for j in range(2, num):
        if (num % j) == 0:
           break
    else:

        print(num, 'is a prime Number')


#First N prime_numbers

N = 11
prime_numbers = []



# If given number is greater than 1
for num in range (2, N+1):

    #Edge case
    if num == 0 or num ==1:
        print(num, 'is not a prime Number')
    else:

        for j in range(2, num):
            if (num % j) == 0:
               break
        else:
            prime_numbers.append(num)
print(prime_numbers)
