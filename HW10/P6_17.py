def isValid(side1, side2, side3):
    if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        return False
    else:
        return True

def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

side1, side2, side3 = eval(input("Enter three sidesin double: "))
if isValid(side1, side2, side3):
    print("The area of the triangle is", area(side1, side2, side3))
else:
    print("Input is invalid")
