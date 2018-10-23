# Rosote.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.width(1)
number_of_circles = int( turtle.numinput("Number of circle",
                                 " How many circles do you want?", 6))
for x in range(number_of_circles):
    t.pencolor("blue")
    t.circle(150)
    t.pencolor("yellow")
    t.circle(130)
    t.pencolor("red")
    t.circle(110)
    t.left(360/number_of_circles)
  
