"""Print numbers in rhombus shape 1 121 12321 121 1"""
# Method1 - only starts:

n = 5
for i in range (n):
    print(" "*(n-i-1) + "* "*(i+1))  # Upper half
for i in range (n-1): #(n-1) bcz we dont need two middle lines
    print(" "*(i+1) + "* "*(n-i-1)) # Lower half

# Method2: -
#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1
from itertools import chain

def up_and_down(n):  # 1,2, ..., n, ..., 2, 1
    return chain(range(1, n), range(n, 0, -1))

def diamond(n):
    for i in up_and_down(n):
        print((n-i)*' ', *up_and_down(i), sep='')
        # or more performant
        # print(''.join(map(str, up_and_down(i))).center(2*n-1))

diamond(5)

# Method3:
 #    1
 #   212
 #  32123
 # 4321234

def rhombus(n):
    for i in range (1, n):
        for j in range (1, n-i+1): # for spaces
            print(end = " ")
        for j in range (i,0,-1): #for spaces
            print(j,end = "")
        for j in range (2,i+1): #for spaces
            print(j,end = "")
        print()
rhombus(5)

# Method4:
 #    1
 #    121
 #   12321
 #  1234321
 # 123454321
 #  1234321
 #   12321
 #    121
 #     1

def rhombus2(n):
    for i in range (1,n+1):
        for j in range (1, n-i+1): # for spaces
            print(end = " ")
        for j in range (1,i+1): #for 2nd triangle
            print(j,end = "")
        for j in range (i-1,0,-1): #for 3rd triangle
            print(j,end = "")
        print()
    for i in range (1,n):
        for j in range (1, i+1): # for spaces
            print(end = " ")
        for j in range (1,n-i+1): #for 2nd triangle
            print(j,end = "")
        for j in range (n-i-1,0,-1): #for 3rd triangle
            print(j,end = "")
        print()
rhombus2(5)
