"""Write a function that takes two lists of strings and return a
list of Strings with all of the intersections of the strings ex:

List1 = {"a","a","a", "b", "d"}
List2 = {"a", "a", "c", "d"}
expectedReturn={"a","a","d"}"""

# Method1:

def intersection(List1, List2):
    List_Intersection = list(set(List1) & set(List2))
    return List_Intersection
List1 = ["a","a","a", "d", "d"]
List2 = ["a", "a", "c", "b","d"]

#Edgecase:
if List1 == List2:
    print("Two lists have are intersection to each other:", List1)
else:
    print(intersection(List1, List2))



# """Intersection of two strings"""
# a = 'geeeks'
# b= 'peeks'

# Method2:
def str_int(a, b):
    c = ""
    # List1 = set(List1)
    n1 = len(a)
    n2 = len(b)
    if n1 < n2:
        for i in a:
            if i in b:
                c +=i

    else:
        for i in b:
            if i in a:
                c +=i
    print(c)

str_int("night", "hot")