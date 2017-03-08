def grade(list, grade):
    best = max(list)
    if grade >= best - 10:
        return "A"
    elif grade >= best - 20:
        return "B"
    elif grade >= best - 30:
        return "C"
    elif grade >= best - 40:
        return "D"
    else:
        return "F"


s = str(input("Enter scores: "))
item = s.split()
list = [eval(x) for x in item]
for i in range(0, len(list)):
    print("Student", i, "score is", list[i], "and grade is", grade(list, list[i]))
