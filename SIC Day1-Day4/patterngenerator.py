#while looking for simple pattern ideas i found out turtle library that lets us draw spirals,stars etc and it intrigues me so it's just thatone of the patters i saw and understood how to do
import turtle
t = turtle.Turtle()   #new turtle object
t.speed(0)          #fastest drawing speed
colors = ["red", "blue", "green", "orange", "purple"]

for i in range(100):
    t.color(colors[i % 5])    #changing colors
    t.forward(i * 2) #moving forward by i*2 units   
    t.right(60) #turning right by 60 degrees

turtle.done()