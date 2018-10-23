# if Spiral.py

answer = input("Do you want to see a spiral? Y/N: ")
colors = ["red", "yellow", "purple", "green", "blue", "brown", "gray"]
if answer == 'y':
print("working...............")
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.speed(0)
t.width(2)
for x in range(100):
        t.pencolor( colors[x%7])
        t.circle(x*2)
        t.left(190)

print("Okay We are done")
