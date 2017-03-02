def getSize(d):
    n = 0
    while d != 0:
        d //= 10
        n += 1
    return n


def getDigit(number):
    if getSize(number) == 2:
        number = number // 10 + number % 10
        return number
    else:
        return number


def getPrefix(number, k):
    if getSize(number) > k:
        for i in range(0, getSize(number) - k):
            number //= 10
        return number
    else:
        return number


def prefixMatched(number, d):
    return d == getPrefix(number, getSize(d))


def sumOfDoubleEvenPlace(number):
    sum = 0
    for i in range(1, getSize(number) + 1):
        if i % 2 == 0:
            sum += getDigit(2 * (number % 10))
        number //= 10
    return sum


def sumOfOddPlace(number):
    sum = 0
    for i in range(1, getSize(number) + 1):
        if i % 2 == 1:
            sum += number % 10
        number //= 10
    return sum


def isValid(number):
    if (13 <= getSize(number) <= 16) and \
            (prefixMatched(number, 4) or prefixMatched(number, 5) or
             prefixMatched(number, 37) or prefixMatched(number, 6)) and \
            ((sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0):
                return True
    else:
        return False


def test():
    number = eval(input("Enter a credit card number: "))
    if isValid(number):
        print("is valid")
    else:
        print("is invalid")


test()
