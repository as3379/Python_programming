def transpose(l1, l2):
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []

        for item in l1:

            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


# Driver code
l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
l2 = []
print(transpose(l1, l2))