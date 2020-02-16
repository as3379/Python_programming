"""how to find the first non-repetitive characters in the String"""
a= 'AAsshrritHa'
a = a.lower() # if capital is not considered.
a_dict={}
for i in a:
    if i not in a_dict:
        a_dict[i] =1
    else:
        a_dict[i] +=1
print(a_dict)

if len(a_dict) == len (a):
    print('All characters are repeating')

for i in a_dict:
    if a_dict[i] ==1:
        print ('First no - repetative character is %s' %i)
        break
