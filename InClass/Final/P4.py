def inBoth(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3


list1 = [1, 2, 3, 4, 5]
list2 = [0, 3, 6, 4, 7, 5]
list3 = inBoth(list1, list2)
print(list1)
print(list2)
print(list3)
