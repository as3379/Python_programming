"""Find Equillibrium Index - Equilibrium index of an array is an index such that the sum of elements at
lower indexes is equal to the sum of elements at higher indexes. """


def equillibrium(arr):
    sum = 0
    left_sum = 0
    n = len(arr)
    for i in range(0, n):
        sum += arr[i]
    print(sum)




    for i in range(0, n):

        sum -= arr[i]

        if left_sum == sum:
            return i
        left_sum += arr[i]


print(equillibrium([-7, 1, 5, 2, -4, 3, 0]))
