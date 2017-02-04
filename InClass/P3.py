num = eval(input("Enter any type of number: "))

if num % 1 == 0:
    if num % 2 == 0:
        if num > 0:
            print("Your number is: even, an integer, positive.")
        elif num == 0:
            print("Your number is: even, an integer, zero.")
        else:
            print("Your number is: even, an integer, negative.")
    else:
        if num > 0:
            print("Your number is: odd, an integer, positive.")
        else:
            print("Your number is: odd, an integer, negative.")
else:
    if num > 0:
        print("Your number is: not an integer, positive.")
    else:
        print("Your number is: not an integer, negative.")
