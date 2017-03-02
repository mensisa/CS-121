def countLetters(s):
    total = 0
    for i in s:
        if i.isspace():
            pass
        else:
            total += 1
    return total

s = str(input("Enter a string: "))
print(countLetters(s))