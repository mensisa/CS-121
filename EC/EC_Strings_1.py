n1 = 34

n2 = -3

n3 = 45.2

n4 = 0.33

# n5 = n1*(n2-n3) + n4/n2
n5 = (float(n1).__mul__(float(n2).__sub__(n3))).__add__(n4.__truediv__(n2))
print(n5)
