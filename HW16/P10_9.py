def deviation(x):
    n = len(x)
    sd = (sum([(i - mean(x)) ** 2 for i in x]) / float(n - 1)) ** 0.5
    return sd


def mean(x):
    n = len(x)
    return sum(x) / float(n)


def main():
    s = str(input("Enter numbers: "))
    items = s.split()
    x = [eval(i) for i in items]
    print("The mean is", mean(x))
    print("The standard deviation is", deviation(x))

main()
