num = eval(input("Enter an integer: "))
a = num // 1000
b = (num - a * 1000) // 100
c = (num - a * 1000 - b * 100) // 10
d = num -a * 1000 - b * 100 - c * 10
r_num = d * 1000 + c * 100 + b * 10 + a
print("The reversed number is", r_num)
