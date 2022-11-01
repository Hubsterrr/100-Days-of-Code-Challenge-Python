from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake with 3 chunks
snake = Snake()

# Create food on screen
food = Food()

# Create scoreboard at the top of the screen
score = ScoreBoard()

# Key listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_point()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    # Detect collision with tail
    for chunk in snake.snake[1:]:
        if snake.head.distance(chunk) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
