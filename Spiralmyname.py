# Spiral My Name

import turtle
t = turtle.Pen()
t.speed(10)
turtle.bgcolor("black")
colors = ["blue", "yellow", "red"]

your_name = turtle.textinput("Enter your name", " what is your name?")

for x in range(150):
    
 t.pencolor( colors[x%3])
 t.penup()
 t.forward(6*x)
 t.pendown()
 t.write(your_name, font = ("Arial", int( (x+4)/4 ), "bold"))
 t.left(190)
