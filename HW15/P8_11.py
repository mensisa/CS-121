def reverse(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    return r


def main():
    s = str(input("Enter a string: "))
    print(reverse(s))

main()
