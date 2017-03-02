def sqrt(n):
    lastGuess = 1
    while True:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        if abs(nextGuess - lastGuess) < 0.0001:
            return nextGuess
            break
        else:
            lastGuess = nextGuess


def test():
    num = eval(input("Enter a number: "))
    print(sqrt(num))


test()
