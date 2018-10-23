# Spiral of Spiral.py

import turtle

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.penup()
t.width(3)

colors = ["red", "purple", "gray", "yellow", "white", "orange", "brown", "white", "green", "blue"]

sides = int(turtle.numinput("Number of sides",
                            "How many sides in your spiral of spirals (2 -6 )", 4, 2, 6))
for x in range(100):
    t.forward(x*4)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    t.width(x/20)

    for m in range(sides):
            t.pendown()
            t.pencolor( colors[ m%sides ])
            t.circle(m/5)
            t.right(360/sides -2)
            t.penup()

            t.setpos(position)
            t.setheading(heading)
            t.left(360/sides + 2)

        
            
