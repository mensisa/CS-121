import random

letter = str(input("Enter a guess (a lowercase letter from a to z): "))
letter = letter.lower()
rand = random.randint(97, 122)

if ord(letter) == rand:
    print("Correct! I choose", chr(rand) + ".")
else:
    print("Wrong! I chose", chr(rand) + ".")