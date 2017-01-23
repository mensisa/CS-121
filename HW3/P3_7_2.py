import time

num = int(format(time.time() * 10000 % 26, ".0f")) + 65

letter = chr(num)

print(letter)