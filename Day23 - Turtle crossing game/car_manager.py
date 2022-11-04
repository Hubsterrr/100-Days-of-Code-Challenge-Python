from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "grey", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 0.5
HEADING = 180


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for _ in range(15):
            car = Turtle()
            car.speed("fastest")
            car.shape("square")
            car.setheading(HEADING)
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            random_x = random.randint(-200, 280)
            car.goto(random_x, random_y)
            self.cars.append(car)
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)

    def generate_cars_offscreen(self):
        if len(self.cars) < 25:
            car = Turtle()
            car.shape("square")
            car.setheading(HEADING)
            car.shapesize(1, 2)
            car.penup()
            random_color = random.choice(COLORS)
            car.color(random_color)
            random_y = random.randint(-240, 240)
            random_x = random.randint(285, 600)
            car.goto(random_x, random_y)
            self.cars.append(car)
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def next_level_speedup(self):
        self.car_speed += MOVE_INCREMENT


