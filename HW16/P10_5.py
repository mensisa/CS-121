num = str(input("Enter ten number: "))
items = num.split()
list1 = [eval(x) for x in items]
list2 = []
for i in range(0, len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
string = ""
for x in list2:
    string += str(x) + " "
print("The distinct numbers are: " + string)
