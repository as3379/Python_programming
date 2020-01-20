#Merge two sorted array:

test_list1 = [1, 4, 6,6, 7, 9, 10]
test_list2 = [1, 2, 3, 5, 5, 6,6, 9,10]

def merge(test_list1, test_list2):

# using naive method
# to combine two sorted lists
    size_1 = len(test_list1)
    size_2 = len(test_list2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if test_list1[i] < test_list2[j]:
          res.append(test_list1[i])
          i += 1

        else:
          res.append(test_list2[j])
          j += 1

    print(i, j)

    res = res + test_list1[i:] + test_list2[j:]

    # printing result
    return str(res)


print ("The combined sorted list is : " + merge (test_list1, test_list2))


#Method2 - Using sorted()

a = test_list1 + test_list2
print(a)
a = sorted(a)
print(a)
