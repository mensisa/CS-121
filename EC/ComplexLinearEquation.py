class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0

    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)


class Complex:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b

    def __add__(self, Complex2):
        return Complex(self.__a + Complex2.__a, self.__b + Complex2.__b)

    def __sub__(self, Complex2):
        return Complex(self.__a - Complex2.__a, self.__b - Complex2.__b)

    def __mul__(self, Complex2):
        return Complex(self.__a * Complex2.__a - self.__b * Complex2.__b,
                       self.__b * Complex2.__a + self.__a * Complex2.__b)

    def __truediv__(self, Complex2):
        return Complex((self.__a * Complex2.__a + self.__b * Complex2.__b) / (Complex2.__a ** 2 + Complex2.__b ** 2),
                       (self.__b * Complex2.__a - self.__a * Complex2.__b) / (Complex2.__a ** 2 + Complex2.__b ** 2))

    def __abs__(self):
        return (self.__a ** 2 + self.__b ** 2) ** 0.5

    def __str__(self):
        if self.__b > 0:
            return "(" + str(self.__a) + " + " + str(self.__b) + "i)"
        elif self.__b == 0:
            return str(self.__a)
        else:
            return "(" + str(self.__a) + " - " + str(abs(self.__b)) + "i)"

    def getRealPart(self):
        return self.__a

    def getImaginaryPart(self):
        return self.__b


a = Complex(0.5, 1)
b = Complex(0.5, -2)
e = Complex(5, 1)
c = Complex(7, 0)
d = Complex(-6, -10)
f = Complex(-7, -7)

l = LinearEquation(a, b, c, d, e, f)

if l.isSolvable():
    print("x = " + str(l.getX()) + " and y = " + str(l.getY()))
else:
    print("The equation has no solution")