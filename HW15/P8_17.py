class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def distance(self, p1):
        return ((self.__x - p1.__x) ** 2 + (self.__y - p1.__y) ** 2) ** 0.5

    def isNearBy(self, p1):
        return self.distance(p1) < 5
    
    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"
    
    
def main():
    x1, y1, x2, y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The distance between the two points is", format(p1.distance(p2), ".2f"))
    if p1.isNearBy(p2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
        
main()
