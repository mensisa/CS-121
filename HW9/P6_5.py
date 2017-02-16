def displaySortedNumbers(num1, num2, num3):
    a = min(num1, num2, num3)
    c = max(num1, num2, num3)
    b = round(num1 + num2 + num3 - a - c, 4)
    print("The sorted numbers are", a, b, c)

num1, num2, num3 = eval(input("Enter three numbers: "))
displaySortedNumbers(num1, num2, num3)
