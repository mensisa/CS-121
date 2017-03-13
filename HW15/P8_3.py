def ispassword(p):
    num_count = 0
    for i in p:
        if i.isdigit():
            num_count += 1
    return len(p) >= 8 and p.isalnum() and num_count >= 2


def main():
    p = str(input("Enter a password: "))
    if ispassword(p):
        print("Valid password")
    else:
        print("Invalid password")

main()
