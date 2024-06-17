from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.color("medium blue")

color = ["medium spring green","purple","blue violet","dark slate blue","gold","black","midnight blue"]
direction = [0, 90, 180, 270]
tim.pensize(15)
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))
    tim.color(random.choice(color))
    tim.speed("fastest")
    

screen = Screen()
screen.exitonclick()