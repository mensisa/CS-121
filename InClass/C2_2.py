import math

radius, length = eval(input("Enter the radius and length of a cylinder: "))
area = radius ** 2 * math.pi
volume = area * length

print("The area is", '{0:.4f}'.format(area), "\nThe volume is", '{0:.2f}'.format(volume))
