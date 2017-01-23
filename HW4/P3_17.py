import turtle

p1x, p1y = eval(input("Enter x and y for p1(Use comma splice x and y): "))
p2x, p2y = eval(input("Enter x and y for p2(Use comma splice x and y): "))
p3x, p3y = eval(input("Enter x and y for p3(Use comma splice x and y): "))

min_x = min(p1x, p2x, p3x)
min_y = min(p1y, p2y, p3y)
s1 = ((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** 0.5
s2 = ((p2x - p3x) ** 2 + (p2y - p3y) ** 2) ** 0.5
s3 = ((p1x - p3x) ** 2 + (p1y - p3y) ** 2) ** 0.5
s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

turtle.penup()
turtle.goto(p1x, p1y)
turtle.pendown()
turtle.write("p1 (" + str(p1x) + ", " + str(p1y) + ")")
turtle.goto(p2x, p2y)
turtle.write("p2 (" + str(p2x) + ", " + str(p2y) + ")")
turtle.goto(p3x, p3y)
turtle.write("p3 (" + str(p3x) + ", " + str(p3y) + ")")
turtle.goto(p1x, p1y)
turtle.penup()
turtle.goto(min_x, min_y - 20)
turtle.pendown()
turtle.write("The area of the triangle is " + format(area, ".1f"))
turtle.hideturtle()

turtle.done()


