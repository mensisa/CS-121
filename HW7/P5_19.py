num = eval(input("Enter the number of lines: "))
for i in range(1, num + 1):
    for j in range(num + 1 - i):
        print(" ", end = "  ")
    for k in range(i, 0, -1):
        print(k, end = "  ")
    for n in range(2, i + 1):
        print(n, end = "  ")
    print()