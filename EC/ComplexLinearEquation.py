from LinearEquation import LinearEquation
from Complex import Complex

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