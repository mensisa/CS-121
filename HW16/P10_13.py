def eliminateDuplicates(lst):
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
    return lst


def main():
    num = str(input("Enter ten number: "))
    items = num.split()
    list1 = [eval(x) for x in items]
    list2 = eliminateDuplicates(list1)
    string = 0
    for x in list2:
        string += str(x) + " "
    print("The distinct numbers are: " + string)

main()
