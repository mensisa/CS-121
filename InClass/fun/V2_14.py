import numpy

for y in numpy.linspace(1.3, -1.1, 40):
    for x in numpy.linspace(-1.1, 1.1, 100):
        if x ** 2 + (5 * y / 4 - abs(x) ** 0.5) ** 2 - 1 <= 0:
            print("$", end="")
        else:
            print(end=" ")
    print()
