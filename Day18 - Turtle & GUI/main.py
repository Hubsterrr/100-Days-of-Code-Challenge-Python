from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color("DarkBlue")



############### Challenge - Generate different shapes with different colours ###############
# triangle - 120
# Square - 90
# pentagon - 72(5)
# hexagon - 60(6)
# heptagon 51.42(7)
# octagon 45 (8)
# nonagon 40 (9)
# decagon 36 (10)
#
# #
#
# angles = [120, 90, 72, 60, 51.42, 45, 40, 36]
# x = 0
# # for angle in angles:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tom.pencolor(r, g, b)
#     for i in range(3 + x):
#         tom.forward(100)
#         tom.right(angle)
#     x += 1

######### challenge - make random coloured path ###########
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     not_a_list = (r, g, b)
#     return not_a_list
#
#
# move = [50, -50]
# turn = [90, -90]
# choice = [0, 1]
#
# for _ in range(400):
#     decision = random.choice(choice)
#     tom.pencolor(random_colour())
#     if decision == 1:
#         tom.forward(random.choice(move))
#     else:
#         tom.right(random.choice(turn))

############### PROJECT - SPIROGRAPH ################
#
#
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colour = (r, g, b)
#     return colour
#
#
# def spirograph(space_between_circles, pen_width):
#     tom.width(pen_width)
#     for i in range(int(360 / space_between_circles)):
#         tom.right(space_between_circles)
#         tom.color(random_colour())
#         tom.circle(300, None, 180)
#
#
# spirograph(5, 10)

############### DAY 18 PROJECT - Hirst Painting ################

import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))

screen = Screen()
tim = Turtle()
screen.colormode(255)
colors = [
    (190, 150, 89), (231, 238, 231), (112, 40, 33), (231, 213, 120), (106, 44, 48),
    (108, 115, 25), (50, 81, 109), (105, 76, 91), (104, 152, 199), (113, 176, 159),
    (57, 54, 53), (179, 150, 68), (43, 74, 51), (41, 63, 95), (168, 201, 212), (167, 98, 95),
    (60, 86, 66), (38, 67, 45), (80, 37, 40), (174, 150, 155), (35, 55, 83),
    (163, 101, 103), (172, 204, 192), (213, 182, 176), (89, 124, 0), (208, 181, 185), (175, 192, 211)
]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setposition(-650, -650)


amount_of_dots = 20
for _ in range(amount_of_dots):
    for _ in range(amount_of_dots):
        tim.dot(40, random.choice(colors))
        tim.forward(70)
    tim.left(90)
    tim.forward(70)
    tim.left(-90)
    tim.setx(-650)

screen.exitonclick()
