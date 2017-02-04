number = 0
for i in range(2001,2101):
    if (i - 2000) % 4 == 0:
        number += 1
        if number % 10 == 0:
            print(i, end = "\n")
        else:
            print(i, end = " ")