def getPentagonalNumber(n):
    return n * (3 * n - 1) / 2

for i in range(1, 101):
    if i % 10 == 0:
        print(format(getPentagonalNumber(i), "<5.0f"), end="\n")
    else:
        print(format(getPentagonalNumber(i), "<5.0f"), end=" ")