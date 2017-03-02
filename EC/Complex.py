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
            return self.__a
        else:
            return "(" + str(self.__a) + " - " + str(abs(self.__b)) + "i)"

    def getRealPart(self):
        return self.__a

    def getImaginaryPart(self):
        return self.__b

# def test():
#     a, b = eval(input("Enter the first complex number: "))
#     c, d = eval(input("Enter the second complex number: "))
#     i1 = Complex(a, b)
#     i2 = Complex(c, d)
#     print(str(i1) + " + " + str(i1) + " = " + str(i1 + i2))
#     print(str(i1) + " - " + str(i1) + " = " + str(i1 - i2))
#     print(str(i1) + " * " + str(i1) + " = " + str(i1 * i2))
#     print(str(i1) + " / " + str(i1) + " = " + str(i1 / i2))
#     print("|" + str(i1) + "|" + " = " + str(abs(i1)))
#
# test()
