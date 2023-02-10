import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
"""Use keyword arguments instead of positional arguments"""
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Your turtle won the race. Congratulations. The {winning_turtle} turtle is the winner")
            else:
                print(f"You lost. The {winning_turtle} turtle is the winner")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
