"""string problem to remove numbers from a mix of numbers and characters"""

def string_replace(s,n):
    S =[]
    N =[]

    #To remove numbers and return characters

    for i in s:
        if i.isalpha():
            S.append(i)
    print(S)
    print(''.join(S))


    #To remove characters and returnn numbers

    for i in n:
        if i.isdigit():
            N.append(i)
    print(N)
    print(''.join(N))

string_replace(s='Ashi13',n='a2s2h')
