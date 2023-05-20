from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
is_race_on = False
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["blue", "red", "green", "yellow", "purple", "orange"]

y_positions = [-150, -100, -50, 0, 50, 100]

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-280, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 268:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've Won! The {winning_turtle} turtle won the race.")
            else:
                print(f"You've lost! The {winning_turtle} turtle won the race.")

        turtle_dist = random.randint(0, 10)
        turtle.fd(turtle_dist)


screen.exitonclick()
