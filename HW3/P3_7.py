import time

a = int(format(time.time() * 10000 % 100, ".0f"))

while (a > 90) | (a < 65):
	a = int(format(time.time() * 10000 % 100, ".0f"))
	
b = chr(a)

print(b)