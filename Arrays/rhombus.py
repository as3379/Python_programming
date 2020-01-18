#Method1:

n = 5
for i in range (n):
    print(" "*(n-i-1) + "* "*(i+1))
for i in range (n-1):
    print(" "*(i+1) + "* "*(n-i-1))

# from itertools import chain
#
# def up_and_down(n):  # 1,2, ..., n, ..., 2, 1
#     return chain(range(1, n), range(n, 0, -1))
#
# def diamond(n):
#     for i in up_and_down(n):
#         print((n-i)*' ', *up_and_down(i), sep='')
#         # or more performant
#         # print(''.join(map(str, up_and_down(i))).center(2*n-1))
#
# print(up_and_down(5))
# # diamond(5)
