T, RH = eval(input("Enter temperature, relative humidity: "))

if T < 80:
    heatIndex = 1.1 * T - 10.3 + 0.047 * RH
else:
    heatIndex = -42.4 + 2.05 * T + 10.14 * RH - 0.225 * T * RH - 0.00684 * T ** 2 - 0.0548 * RH ** 2 + \
        0.00123 * RH * T ** 2 + 0.000853 * T * RH ** 2 - 0.00000199 * T ** 2 * RH ** 2

print("The Heat Index =", heatIndex)
