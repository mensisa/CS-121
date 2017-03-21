import random


def shuffle(lst):
    lst1 = []
    while lst:
        index = random.randint(0, len(lst) - 1)
        item = lst.pop(index)
        lst1.append(item)
    return lst1


def main():
    num = str(input("Enter a list separated by space : "))
    items = num.split()
    lst = [eval(x) for x in items]
    result = ""
    for i in shuffle(lst): result += str(i) + " "
    print("Thr new list is:", result)

main()
