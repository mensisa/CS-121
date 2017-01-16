import turtle
import math

#cx, cy = eval(input("Enter center x,y: "))
#radius = eval(input("Enter the radius: "))
cx = 50
cy = 50
radius = 100

turtle.penup()
turtle.goto(cx, cy - radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(cx, cy)
turtle.pendown()
turtle.write("Area:" + str(round(math.pi * radius ** 2)))
    
turtle.done()
