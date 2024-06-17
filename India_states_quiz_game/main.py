import pandas
import turtle


screen = turtle.Screen()
screen.title("India States Game")  # Sets the title of the window
image = "google.gif"  # Shown below
screen.addshape(image)
turtle.shape(image)
screen.setup(700, 700)
def mouse_click_coords(x, y):
    print(x, y)
    screen.onscreenclick(mouse_click_coords)
    turtle.mainloop()

data = pandas.read_csv("India.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
screen.exitonclick()