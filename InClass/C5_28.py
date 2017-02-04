e = 0
n = 1
for i in range(100000):
    n = n * i
    if i == 0:
        n = 1
    e += 1/n
    if i % 10000 == 0:
        print(e)
