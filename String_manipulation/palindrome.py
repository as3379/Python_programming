#Slicing
def palindrome():
    original = input('enter the string: ')
    reverse = original[::-1]
    if (original==reverse):
        return True
    else:
        return False

ans = palindrome()
if ans ==1 :
    print("String is palindrome")
else:
    print("String is not palindrome")
