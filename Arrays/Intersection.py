"""Write a function that takes two lists of strings and return a list of Strings with all of the intersections of the strings ex:

List1 = {"a","a","a", "b", "d"}
List2 = {"a", "a", "c", "d"}
expectedReturn={"a","a","d"}"""

# Method1:

def intersection(List1, List2):
    List_Intersection = list(set(List1) & set(List2))
    return List_Intersection
List1 = ["a","a","a", "b", "d"]
List2 = ["a", "a", "c", "d"]
print(intersection(List1, List2))


# """Intersection of two strings"""
# a = 'geeeks'
# b= 'peeks'

# Method2:

c = []
List1 = set(List1)
for i in List1:
    if i in List2:
        c.append(i)
print(c)
