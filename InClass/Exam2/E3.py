def getLast(n):
    if 0 < abs(n) < 10:
        return n
    else:
        return n % 10


def getFirst(n):
    if 0 < abs(n) < 10:
        return n
    else:
        while abs(n) >= 10:
            n //= 10
        return n


def getEnds(n):
    return getFirst(n) * 10 + getLast(n)


def main():
    n = eval(input("Enter a number: "))
    print("The new number is", getEnds(n))

main()

