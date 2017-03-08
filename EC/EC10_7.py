import random

n = 0
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n < 1000:
    num = random.randint(0, 9)
    counts[num] += 1
    n += 1
print(counts)
