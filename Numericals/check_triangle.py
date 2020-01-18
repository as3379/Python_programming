"""Given sides of a triangle write a function
which could say it is equilateral , isosceles or scalene.
Give Test data for the solution you give"""


def triangle (x , y, z ):
    if ((x+y<=z) or (y+z<=x) or (z+x<=y)):
        print('It is not a triangle')
    elif (x==y and y ==z):
        print('It is a Equilateral triangle')
    elif (x==y or y==z or z==x):
        print('It is isoloceles triangle')
    else:
        print('It is a scalene triangle')

triangle(5,6,7)
