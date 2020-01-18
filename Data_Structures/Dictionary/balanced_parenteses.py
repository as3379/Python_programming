
def balanced(a):

    if len(a)%2 !=0:
        return False
    b = set('([{')
    matches = set ([ ('(',')'), ('[',']'), ('{','}') ])

    s = []


    for paren in a:
        if paren in b:
            s.append(paren)
        else:
            # Add the word to dictionary with count 1
            if len(s) == 0:
                return False
            last_open = s.pop()

            if (last_open, paren) not in matches:
                return False
    return len(s) == 0




a = '[]}({)'
print(balanced(a))




# for i in list(d.keys()):
#     if
#     print(key, ":", d[key])
