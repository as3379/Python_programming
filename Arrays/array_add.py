def add_one(arr):

    "".join(arr)
    print(arr)

    n = len(arr)
    number = 0

    for i in range(0,n):
        number += arr[i]*(10**(n-i-1))
    print(number)

    number = number + 1
    number = str(number)
    new_arr = list(map(int, str(number)))


    print(new_arr)



add_one(arr = [1,2,3])
