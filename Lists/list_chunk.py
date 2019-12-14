def divide_chunks(my_list, l, n):

    # looping till length
    for i in range(0, l, n):
        yield my_list[i:i + n]
    return my_list

# How many elements each
# list should have

my_list = [1, 2, 3, 4, 5,
              6, 7, 8, 9]

l = len(my_list)
n = 4
x = list(divide_chunks(my_list, l, n ))
print (x)
if l%n ==0:
    n1 = l//n
else:
    n1 = (l//n) +1
final = [my_list[i * n:(i + 1) * n] for i in range(n1)]
print (final)
