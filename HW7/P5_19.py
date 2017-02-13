num = eval(input("Enter the number of lines: "))
if 0 < num <= 15:
    for i in range(1, num + 1):
        print("   " * (num - i), end="")
        for j in range(i, 0, -1):
            print(j, end="  ")
        for k in range(2, i + 1):
            print(k, end="  ")
        print()
else:
    print("Number of lines should from 1 to 15")
