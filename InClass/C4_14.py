import random

guess = eval(input("Head(0) or tail(1): "))
coin = random.randint(0,1)

print(guess == coin)