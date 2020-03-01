"""Given coordinates of bottom-left and top-right corners of a rectangle. Check if a point (x, y)
lies inside this rectangle or not.

"""
def inside_out(x1,y1, x2,y2, x,y):
    if (x > x1 and x < x2 and y > y1 and y < y2) :
        return True
    else:
        return False

# Driver code
print(inside_out(0,0, 10,8, -1,-1))