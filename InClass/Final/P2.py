n1, n2 = eval(input("Enter n1 and n2: "))
if n1 > n2:
    print(n1 + n2)
elif n1 < n2:
    if n2 % 10 == 0:
        print(n1 / n2)
    else:
        print(n1 * n2)