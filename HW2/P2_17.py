weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))
print("BMI is", 0.45359237 * weight / ((0.0254 * height) ** 2))