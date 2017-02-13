def m(i):
    total = 0
    for n in range(1, i + 1):
        total += n / (n + 1)
    return total

print(format("i", "<15s"), format("m(i)", "<15s"))
for i in range(1, 21):
    print(format(i, "<15d"), format(m(i), "<15.4f"))
