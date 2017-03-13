def solveQuadratic(eqn, roots):
    a, b, c = eqn[0], eqn[1], eqn[2]
    discriminant = b ** 2 - 4 * a * c
    r1 = (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    roots = [r1, r2]
    if discriminant > 0:
        print("The roots are", roots[0], "and", roots[1])
        return 2
    elif discriminant == 0:
        print("The root is", roots[0])
        return 1
    else:
        print("The equation has no real roots")
        return 0


def main():
    eqn = eval(input("Enter a, b, c:"))
    solveQuadratic(eqn, [])

main()
