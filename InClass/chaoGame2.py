import random
import turtle

#p1
x1 = 200
y1 = 200
#p2
x2 = 200
y2 = -200
#p3
x3 = -200
y3 = -200
#p4
x4 = -200
y4 = 200

x_min = min(x1, x2, x3, x4)
x_max = max(x1, x2, x3, x4)
y_min = min(y1, y2, y3, y4)
y_max = max(y1, y2, y3, y4)
x = random.randint(x_min, x_max)
y = random.randint(y_min, y_max)
turtle.speed(0)

n = 2
list = [1, 3]
while n < 30000:
    p = random.randint(1, 4)
    list.append(p)
    while abs(list[n - 1] - p) != 2 or abs(list[n - 2] - p) != 2 or abs(list[n - 1] - p) != 0 or abs(list[n - 2] - p) != 0:
        p = random.randint(1, 4)
        list[n] = p
    else:
        if p == 1:
            xTarget = x1
            yTarget = y1
        if p == 2:
            xTarget = x2
            yTarget = y2
        if p == 3:
            xTarget = x3
            yTarget = y3
        if p == 4:
            xTarget = x4
            yTarget = y4

    x = (x + xTarget) / 2
    y = (y + yTarget) / 2
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(1)
    n += 1
turtle.done()