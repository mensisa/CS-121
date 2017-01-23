import turtle

turtle.begin_fill()
turtle.color("red")
turtle.left(30)
turtle.circle(150, steps = 6)
turtle.end_fill()
turtle.right(30)

turtle.penup()
turtle.goto(-150,90)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", font = ("Time", 60, "bold"))
turtle.hideturtle()

turtle.done()
