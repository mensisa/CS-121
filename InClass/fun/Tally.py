class Tally:
    def __init__(self, number=0):
        self.__number = int(number)

    def __add__(self, tally2):
        return Tally(self.__number + tally2.__number)

    def __sub__(self, tally2):
        return Tally(self.__number - tally2.__number)

    def __mul__(self, tally2):
        return Tally(self.__number * tally2.__number)

    def __truediv__(self, tally2):
        return Tally(self.__number / tally2.__number)

    def __str__(self):
        return Tally.__fives(self) * (self.__number // 5) + "|" * (self.__number % 5)

    def __fives(self):
        return u'\u2020' * 5 + " "


def test():
    n = Tally(2)
    m = Tally(11)
    print(n)
    print(m)
    print(n, "*", m, "=", n * m)
    print(n, "+", m, "=", n + m)
    print(m, "/", n, "=", m / n)
    for i in range(20):
        print(i, Tally(i))


test()
