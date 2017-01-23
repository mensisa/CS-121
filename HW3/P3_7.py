import time

num = int(format(time.time() * 10000 % 100, ".0f"))

while (num > 90) | (num < 65):
	num = int(format(time.time() * 10000 % 100, ".0f"))
	
letter = chr(num)

print(letter)