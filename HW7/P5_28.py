e = 1
n = 1
for i in range(1, 100001):
    n = n * i
    e += 1/n
    if i % 10000 == 0:
        print(e)