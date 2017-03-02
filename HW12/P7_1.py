class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height


def test(width, height):
    r = Rectangle(width, height)
    print(format(str(r.width), "7s"), format(str(r.height), "7s"),
          format(str(r.getArea()), "7s"), format(str(r.getPerimeter()), "7s"))


def main():
    test(4, 40)
    test(3.5, 35.9)

main()
