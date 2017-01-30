amount = eval(input("Enter an amount, for example, 11.56: "))

remainingAmount = amount * 100

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consists of")
if numberOfOneDollars > 1:
    print("\t", numberOfOneDollars, "dollars")
elif numberOfOneDollars == 1:
    print("\t", numberOfOneDollars, "dollar")
if numberOfQuarters > 1:
    print("\t", numberOfQuarters, "quarters")
elif numberOfQuarters == 1:
    print("\t", numberOfQuarters, "quarter")
if numberOfDimes > 1:
    print("\t", numberOfDimes, "dimes")
elif numberOfDimes == 1:
    print("\t", numberOfDimes, "dime")
if numberOfNickels > 1:
    print( "\t", numberOfNickels, "nickels")
elif numberOfNickels == 1:
    print("\t", numberOfNickels, "nickel")
if numberOfPennies > 1:
    print( "\t", numberOfPennies, "pennies")
elif numberOfPennies == 1:
    print("\t", numberOfPennies, "penny")