import turtle as t 
import random
from turtle import Turtle,Screen

tim = Turtle()
color = ["red","blue","orange","pink","black","green","brown","yellow","purple","violet"]
tim.shape("arrow")
tim.pensize(3)
tim.color(random.choice(color))

tim.speed("fastest")
for _ in range(40):
    tim.color(random.choice(color))
    tim.circle(100)
    tim.setheading(tim.heading() + 10)

screen = Screen()
screen.exitonclick()