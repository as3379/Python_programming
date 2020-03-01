"""Print middle character of a string. If middle value has even then print 2 characters

Eg: Amazon -->print az """


def middle_char(S):

    S = S.replace(" ", "")
    # mid = ""

    n = len(S)
    if n%2 ==0:
        mid = S[n//2 -1]+ S[n//2]
    else:
        mid = S[n//2 -1]


    print(mid)

middle_char("Amazon")
middle_char("Amazonprime")
middle_char("Amazon prime")
