# Viral Family

import turtle

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.penup()
t.width(3)

colors = ["red", "purple", "gray", "yellow", "white", "orange", "brown", "white", "green", "blue"]

family = []
name = turtle.textinput("My family",
                        "Enter a name, or just hit [Enter] to end")

while name != " ":
        family.append(name)
name = turtle.textinput("My family",
                        "Enter a name, or just hit [Enter] to end")


for m in range(100):
             t.forward(m*4)
             position = t.position()
             heading = t.heading()

for n in range(len(family)):
            t.pendown()
            t.pencolor(color[n% len(family)%10])
            t.write(family[n%len(family)], font =("Arial", int((m+4)/4), "bold"))
            t.right(360/len(family))
            t.width(m/20)
            t.penup()
            t.forward(m/2)
            t.setposition(position)
            t.setheading(heading)
            t.left(360/len(family) +3)


