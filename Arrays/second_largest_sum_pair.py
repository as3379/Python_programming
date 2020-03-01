"""How to find the second largest sum of any two pairs in an array of numbers"""

# Method1: Using sort and Iterator

A = [1, 4, 5, 3, 2, 1]

A = sorted(A)
# print(A)

#  5 + 4 = 9
#  5 + 4= 9
#  5 + 3 = 8
#  4 + 4 = 8
n = len(A)
B = []
# print("What is the last element of A: ", A[-1])

for i in range(1, n):
    for j in range(2, n-1):

        if (A[-i], A[-j]) not in B:
            B.append((A[-i], A[-j]))

print(B)


# # Method2: find max and sec_max
#
#
# def max_pairs(a):
#     # arr = [1, 2, 6, 4, 5]
#     s = []
#     n = len(a)
#     for i in range(0, 2):
#         m = max_one(a)
#         a.remove(m[1])
#
#     #
#     return m
#
#
# def max_one(a):
#     sec_max = 0
#     max = 0
#     m = []
#     n = len(a)
#     for i in range(0, n):
#         if a[i] > max:
#             max = a[i]
#         sec_max = a[i]
#
#     m.append(max)
#     m.append(sec_max)
#
#     return m
#
#
# print(max_pairs([1, 4, 5, 3, 2, 1]))
#
