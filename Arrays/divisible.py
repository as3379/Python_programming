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
