# Method1 - Pop and append
def palindrome():
    original = input('enter the string: ')
    a = list(original)
    print(a)
    n = len(a)
    b =[]
    for i in range(0,n):
        p = a.pop(-1)
        b.append(p)
    b = "".join(b)
    print(b)

    if (original==b):
        return True
    else:
        return False

print(palindrome())

#
# # Method1 - Slicing
# def palindrome():
#     original = input('enter the string: ')
#     reverse = original[::-1]
#     if (original==reverse):
#         return True
#     else:
#         return False
#
# ans = palindrome()
# if ans ==1 :
#     print("String is palindrome")
# else:
#     print("String is not palindrome")
#
# # Method2- Iterative
# def isPalindrome(str):
#
#     # Run loop from 0 to len/2
#     for i in xrange(0, len(str)/2):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")
#
# #Method3 - looping
# def palindrome2():
#     s = input('enter the string: ')
#     s = list(s)
#     n = len(s)
#     reverse =[]
#     for i in range (0, n):
#       reverse.append(s[n-1])
#       n -= 1
#     print (reverse)
#     if s == reverse:
#         print("String is palindrome")
#     else:
#         print("String is not palindrome")
#
# palindrome2()
