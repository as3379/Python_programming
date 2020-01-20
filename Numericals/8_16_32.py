"""Write a function in any language that will print "AN"
if a number is divisible by 8, "ANIM" if divisible by 16 and "ANIMAL"
if divisible by 32."""

#Method1

def divisible(n):

    #Edge case
    if n%8 ==0 and n%16 ==0 and n%32 ==0:
        print('Number  is dividible by all three - 8, 16, 32')
    else:


        if n%8 ==0:
            print('AN - Number divisible by 8 ')
        if n%16 ==0:
            print('ANIM - Number divisible by 16')
        if n%32 ==0:
            print('ANIMAL - Number divisible by 32')

divisible(16)


#Method2

n = input('Enter the number: ')
n = int(n)
if n % 32 == 0:
    if n % 16 == 0:
         print("ANIMAL && ANIM")

    elif n % 8 == 0:
         print("ANIMAL && AN")
    else:
        print("ANIMAL")

elif n % 16 == 0:
    if n % 8 == 0:
         print("ANM && AN")
    else:
        print ("ANM")

elif n % 8 == 0:
    print("AN")

else:
    print("Number is not divisible by 8 or 16 or 32")
