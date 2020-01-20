
def int_to_string(integer):

    #check if it is a negative number
    if integer < 0:
        integer = -1*integer
        print('number is negative')
        is_neagative = True
    else:
        print('number is positive')
        is_neagative = False

    output = []
    while integer > 0:

        output.append(chr(ord('0')+ integer % 10))
        integer //= 10

    z = ''.join(reversed(output))

    if is_neagative == True:
        z = '-' + z


    print(z, type(z))

integer = -1023
int_to_string(integer)
