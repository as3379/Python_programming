
"""Find if two rectangles overlap"""


def doOverlap(l1x, l1y, r1x,r1y, l2x,l2y,r2x,r2y):
    # If one rectangle is on left side of other
    if (l1x > r2x or l2x > r1x):
        return False

    # If one rectangle is above other
    if (l1y < r2y or l2y < r1y):
        return False

    return True

print(doOverlap(0, 10,10, 0,11, 5,15, 0))