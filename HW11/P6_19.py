def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    return True if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) > 0 else False


def onTheSameLine(x0, y0, x1, y1, x2, y2):
    return True if (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) == 0 else False


def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    if onTheSameLine(x0, y0, x1, y1, x2, y2):
        return True if min(x0,x2) <= x2 <= max(x0, x1) and min(y0,y2) <= y2 <= max(y0, y1) else False
    else:
        return False


def test():
    x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2: "))
    if leftOfTheLine(x0, y0, x1, y1, x2, y2):
        print("on the left side")
    elif onTheSameLine(x0, y0, x1, y1, x2, y2):
        if onTheLineSegment(x0, y0, x1, y1, x2, y2):
            print("on the line segment")
        else:
            print("on the same line")
    else:
        print("on the right side")

test()

# 3.4,2,6.5,9.5,-5,4
# 1,1,5,5,2,2
# 3.4,2,6.5,9.5,5,2.5