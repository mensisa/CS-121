a, b, c = eval(input("Enter three edges: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("The input is invalid")
else:
    print("The perimeter is", a + b + c)
