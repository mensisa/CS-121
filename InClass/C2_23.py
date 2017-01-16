import turtle

radius = eval(input("Enter the radius: "))

turtle.penup()
turtle.forward(radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.right(180)
turtle.forward(2*radius)
turtle.right(180)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.right(90)
turtle.forward(2*radius)
turtle.left(90)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.forward(2*radius)
turtle.pendown()
turtle.circle(radius)

turtle.down()
