num = str(input("Enter integers between 1 and 100: "))
items = num.split()
list1 = [eval(x) for x in items]
list2 = []
for i in range(0, len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
list2.sort()
for i in list2:
    count = list1.count(i)
    if count == 1:
        print(str(i) + " occurs " + str(count) + " time")
    else:
        print(str(i) + " occurs " + str(count) + " times")