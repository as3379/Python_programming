"""Amazon Coding Interview Question - Recursive
Staircase Problem or fibinocci series"""

#Method1: Recursion
def num_ways(n):
    if n ==0 or n==1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

print(num_ways())

#Method2: Dynamic programming
def num_ways_dp(n):

    a = [0] * (n+1)
    a[0]= 1
    a[1]= 1
    if n ==0 or n==1:
        print(1)

    for i in range(2, n+1):

        a[i] = a[i-1] + a[i-2]

    print(a)


"""Staircase Problem if steps are specified"""

#Method1: Recursion

def findStep( n) :
    total = 0
    b = {1,2,3}
    if (n == 0) :
        return 1

    else :
        for i in b:
            if n -i >= 0:
                total +=findStep(n-i)

    return total

# Driver code
n = 4
print(findStep(n))

#Method2: Dynamic programming

def cjo(n):
    a = [0]* (n+1)
    a[0] = 1

    for i in range(1, n+1):
        total = 0
    for j in {1, 3, 5}:
        if i-j >=0:
            total += a[i-j]
    a[i] = total
    return total, a
print(cjo(4))