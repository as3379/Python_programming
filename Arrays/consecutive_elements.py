"""Check if array elements are consecutive."""

#Method1: using sort

def consecutive1(a):
    a = sorted(a)
    b = set(a)

    #edgecase:
    if len(a) > len(b):
        return False
    else:
        for i in range (0, len(a)-1):
            if a[i+1] - a[i] == 1:
                continue
            else:
                return False
        return True


def consecutive2(a):
     b = min(a)
     c = max(a)
     # print(b, c)
     n = len(a)

     b = set(a)

     # edgecase:
     if len(a) > len(b):
         return False
     else:
         for i in range(b,c):
             if b+1 in a:
                 b +=1
             else:
                # print("Array is not consecutive")
                return False
     return True


print(consecutive1([5, 2, 3, 1, 4,6,4]))
print(consecutive2([5, 2, 3, 1, 4, 4, 6]))