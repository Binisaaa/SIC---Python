import turtle
import random
t = turtle.Turtle()
t.speed(0)
t.color("brown")
t.write("Happy Birthday!", font=("Arial", 30, "bold"))
t.forward(100)
t.color("red","pink")
t.begin_fill()         
t.penup()
t.goto(0, -100)          
t.left(140)              
t.forward(-180)           
t.circle(-90, 200)       
t.left(120)              
t.circle(-90, 200)       
t.forward(180)           
t.end_fill()             

t.hideturtle()
turtle.done()

