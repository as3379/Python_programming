# Method1

def finder(s):

    s = list(s)

    count = {}

    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for k in count:
        if count[k] > 1:
            return False

    return True

s = 'Ashritha'

#1, 0, 4
print(finder(s))


# Method2 - Create a set of string ang compare the length of set with original new_string
def finder2(s):

    return (len(set(s))==len(s))

print(finder2(s))
