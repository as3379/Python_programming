
def string_to_int(s):

    #check if it is a negative number
    if s[0] == '-':
        start_index = 1
        print('number is negative')
        is_neagative = True
    else:
        start_index = 0
        print('number is positive')
        is_neagative = False

    n = len(s)
    z = 0
    for i  in range(start_index,n):
        x = 10**(n-(i+1))
        y = ord(s[i]) - ord('0')
        z += x * y

    if is_neagative == True:
        z = -1*z


    print(z)

s = '-1023'
string_to_int(s)
