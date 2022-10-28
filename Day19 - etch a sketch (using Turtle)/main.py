import random
from turtle import Turtle, Screen

#
# tom = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tom.forward(10)
#
#
# def move_backwards():
#     tom.back(10)
#
#
# def turn_clockwise():
#     tom.right(10)
#
#
# def turn_counter_clockwise():
#     tom.left(10)
#
#
# def reset():
#     screen.reset()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(turn_counter_clockwise, "a")
# screen.onkey(reset, "c")

################## DAY 19 - TURTLE RACE GAME ##################

screen = Screen()

screen.setup(width=500, height=400)

counter = 0
start_x = -230
start_y = -150
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race = []
finish_line = 230

# Preparation for the race
for one_color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(one_color)
    new_turtle.penup()
    new_turtle.goto(x=start_x, y=start_y)
    start_y += 60
    race.append(new_turtle)

# Asking user for a bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()

# Race
is_winner = False
while not is_winner:
    turtle = random.choice(race)
    turtle.forward(random.randint(1, 10))
    turtle_position = list(turtle.position())
    if turtle_position[0] >= finish_line:
        is_winner = True
        turtle_color = turtle.pencolor()
        if turtle_color == user_bet:
            print("You win")
        else:
            print(f"You lose. The winner was: {turtle_color}")

screen.exitonclick()
