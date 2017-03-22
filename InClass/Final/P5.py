def interleave(lst1, lst2):
    lst3 = []
    n = len(lst1) if len(lst1) < len(lst2) else len(lst2)
    for i in range(0, n):
        lst3.append(lst1[i])
        lst3.append(lst2[i])
    return lst3


test1 = [1, 2, 3, 4, 5, 0, 0]
test2 = [9, 8, 7, 6]

test3 = interleave(test1, test2)
print(test3)
