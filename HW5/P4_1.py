a, b, c = eval(input("Enter a, b, c: "))

discriminant = b ** 2 - 4 * a * c
r1 = (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) /(2 * a)
r2 = (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) /(2 * a)

if discriminant > 0:
    print("The roots are", r1, "and", r2)
elif discriminant == 0:
    print("The root is", r1)
else:
    print("The equation has no real roots")