import random
import turtle

x = 0.0
y = 0.0
# Stem
f1 = [0, 0, 0, 0.16, 0, 0, 0.01]
# Successively smaller leaflets
f2 = [0.85, 0.04, -0.04, 0.85, 0, 1.60, 0.85]
# Largest left hand leaflet
f3 = [0.20, -0.26, 0.23, 0.22, 0, 1.60, 0.07]
# Largest right hand leaflet
f4 = [-0.15, 0.28, 0.26, 0.24, 0, 0.44, 0.07]
# Probability
p1, p2, p3, p4= f1[6], f1[6] + f2[6], f1[6] + f2[6] + f3[6], f1[6] + f2[6] + f3[6] + f4[6]

turtle.tracer(0)

for i in range(20000):
    if i % 1000 == 0:
        turtle.update()
    rand = random.random()
    if rand < p1:
            x = f1[0] * x + f1[1] * y + f1[4]
            y = f1[2] * x + f1[3] * y + f1[5]
    if p1 <= rand <= p2:
            x = f2[0] * x + f2[1] * y + f2[4]
            y = f2[2] * x + f2[3] * y + f2[5]
    if p2 < rand <= p3:
            x = f3[0] * x + f3[1] * y + f3[4]
            y = f3[2] * x + f3[3] * y + f3[5]
    if p3 < rand < p4:
            x = f4[0] * x + f4[1] * y + f4[4]
            y = f4[2] * x + f4[3] * y + f4[5]
    turtle.penup()
    turtle.goto(x * 35, y * 35)
    turtle.pendown()
    turtle.forward(1)
turtle.done()
