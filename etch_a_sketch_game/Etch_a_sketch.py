from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("medium blue")
tim.speed("fastest")
screen = Screen()


def move_forward():
    tim.forward(50)
    tim.pensize(9)


def move_backward():
    tim.backward(50)
    tim.pensize(9)


def turn_left():
    tim.setheading(tim.heading() + 50)
    tim.pensize(9)


def turn_right():
    tim.setheading(tim.heading() - 50)
    tim.pensize(9)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()