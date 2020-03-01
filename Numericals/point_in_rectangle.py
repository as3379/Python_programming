"""Given four points of a rectangle, and one more point P. Write a function to check whether
P lies within the given rectangle or not."""

def area (x1, y1, x2, y2, x3, y3):

    A = abs ((x1*(y2-y3) + x2*(y3-y1) +x3*(y1-y2))/2.0)
    return A

x1,y1, x2, y2, x3, y3, x4, y4, x, y = 0, 10, 10, 0, 0, -10,-10, 0, 1, 2

A = (area(x1, y1, x2, y2, x3, y3) +
     area(x1, y1, x4, y4, x3, y3))

# Calculate area of triangle PAB
A1 = area(x, y, x1, y1, x2, y2)

# Calculate area of triangle PBC
A2 = area(x, y, x2, y2, x3, y3)

# Calculate area of triangle PCD
A3 = area(x, y, x3, y3, x4, y4)

# Calculate area of triangle PAD
A4 = area(x, y, x1, y1, x4, y4);

# Check if sum of A1, A2, A3
# and A4 is same as A
if (A == A1 + A2 + A3 + A4):
    print("Point is inside rectangle")
else:
    print("Point is outside rectangle")


