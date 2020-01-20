

def anagram(a, b):

    a = a.lower().replace(' ', '')
    b = b.lower().replace(' ', '')
    count = {}

    #Edge case:
    if len(a) != len(b):
        return False

    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print (count)
    for j in b:
        if j in count:
            count[j] -= 1
        else:
            count[j] = 1
    print (count)

    for k in count:

        if count[k] != 0:
            return False

    return True

a = 'Beeer'
b = 'Beer'
print(anagram(a, b))
