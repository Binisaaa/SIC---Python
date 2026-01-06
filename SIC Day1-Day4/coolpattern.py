#one more turtle patter made by myself
import turtle
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "green", "blue", "purple", "pink"]
for i in range(50):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.left(59)
    t.circle(i / 4)
    t.forward(-i)
length = 200
angle = 90
t.color("black")
for j in range(50):
    t.forward(-length)
    t.left(angle)
    length -= 4
t.forward(-500)
t.color("blue")
for k in range(50):
    t.circle(k * 3)
    t.left(10)
turtle.done()