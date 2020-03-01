"""Given two overlapping rectangles on a plane. We are given bottom left and top right points of the two rectangles.
we need to find the area of overlapping rectangle"""

def area_overlap(x1, y1, x2, y2, x3, y3, x4, y4):



    x = abs (max(x1, x3) - min(x2,x4))
    y = abs (max(y1, y3) - min(y2,y4))

    area = x*y
    total_area = abs(x1 - x2) * abs(y1 - y2) + abs(x3 - x4) * abs(y3 - y4) - area

    return area, total_area
print(area_overlap(2, 2 , 5, 7, 3, 4, 6, 9))


