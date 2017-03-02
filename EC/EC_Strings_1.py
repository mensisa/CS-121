n1 = 34

n2 = -3

n3 = 45.2

n4 = 0.33

# n5 = n1*(n2-n3) + n4/n2
a = n2.__sub__(n3)
b = n1.__mul__(a)
c = n4.__truediv__(n2)
n5 = a.__add__(c)
print(n5)
