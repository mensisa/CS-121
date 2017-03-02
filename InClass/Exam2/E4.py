class Box:
    def __init__(self, length=1.0, width=2.0, height=3.0):
        self.__length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.__length * self.width * self.height

    def surfaceArea(self):
        return 2 * (self.__length * self.width + self.width * self.height + self.height * self.__length)

    def scale(self, multiplier):
        self.__length *= multiplier
        self.width *= multiplier
        self.height *= multiplier


def main():
    box1 = Box()
    print(box1.volume(), box1.surfaceArea())
    box2 = Box(4, 5, 10)
    print(box2.volume(), box2.surfaceArea())
    box2.scale(0.5)
    print(box2.volume(), box2.surfaceArea())

main()
