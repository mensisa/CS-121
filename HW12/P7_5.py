import math


class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        return (self.__n * self.__side ** 2) / (4 * math.tan(math.pi / self.__n))


def test():
    rp = RegularPolygon()
    print(rp.getPerimeter(), rp.getArea())
    rp = RegularPolygon(6, 4)
    print(rp.getPerimeter(), rp.getArea())
    rp = RegularPolygon(10, 4, 5.6, 7.8)
    print(rp.getPerimeter(), rp.getArea())

test()
