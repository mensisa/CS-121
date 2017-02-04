import random
import turtle

#p1
x1 = 0
y1 = 200
#p2
x2 = 200
y2 = -100
#p3
x3 = -200
y3 = -100

x_min = min(x1, x2, x3)
x_max = max(x1, x2, x3)
y_min = min(y1, y2, y3)
y_max = max(y1, y2, y3)
x = random.randint(x_min, x_max)
y = random.randint(y_min, y_max)
turtle.tracer(0)

for i in range(20000):
    p = random.randint(1, 3)
    if i % 1000 == 0:
        turtle.update()
    if p == 1:
        xTarget = x1
        yTarget = y1
    elif p == 2:
        xTarget = x2
        yTarget = y2
    else:
        xTarget = x3
        yTarget = y3

    x = (x + xTarget) / 2
    y = (y + yTarget) / 2
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(1)
turtle.done()