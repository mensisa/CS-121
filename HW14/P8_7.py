def getNumber(uppercaseLetter):
    if uppercaseLetter in "ABC":
        return 2
    elif uppercaseLetter in "DEF":
        return 3
    elif uppercaseLetter in "GHI":
        return 4
    elif uppercaseLetter in "JKL":
        return 5
    elif uppercaseLetter in "MNO":
        return 6
    elif uppercaseLetter in "PQRS":
        return 7
    elif uppercaseLetter in "TUV":
        return 8
    elif uppercaseLetter in "WXYZ":
        return 9


def main():
    string = str(input("Enter a string: "))
    for i in range(0, len(string)):
        if string[i].isalpha():
            string = string.replace(string[i], str(getNumber(string[i].upper())), 1)
    print(string)

main()

