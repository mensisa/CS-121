def isSSN(ssn):
    ssn = ssn.replace("-", "")
    for i in ssn:
        if i.isdigit() and len(ssn) == 9:
            return True
        else:
            return False
            break


def main():
    ssn = str(input("Enter a string for SSN: "))
    if isSSN(ssn):
        print("Valid SSN")
    else:
        print("Invalid SSN")

main()
