integer = -1
positive = 0
negative = 0
count = 0
sum = 0

while integer != 0:
    count += 1
    integer = eval(input("Enter an integer, the input end if it is 0: "))
    if integer > 0:
        positive += 1
    elif integer < 0:
        negative += 1
    sum += integer
if count > 0:
    print("The number of positives is", positive,
          "\nThe number of negative is", negative,
          "\nThe total is", sum,
          "\nThe average is", sum / (count - 1))
else:
    print("You didn't enter any number")
