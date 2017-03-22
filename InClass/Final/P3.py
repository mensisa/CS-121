def uniqueList(list1):
    list2 = list1[:]
    for i in list1:
        while list2.count(i) > 1:
            list2.remove(i)
    list2.sort()
    return list2


list1 = [1, 2, 3, 4, 5, 1, 2, 3]
list2 = uniqueList(list1)
print(list1)
print(list2)
