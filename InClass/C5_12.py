number = 0
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0:
        number += 1
        if number % 10 == 0:
            print(i, end = "\n")
        else:
            print(i, end = " ")