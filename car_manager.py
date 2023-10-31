import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_RANGE = 230
MIN_RANGE = -230


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.generate()

    def generate(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            y_position = random.randint(MIN_RANGE, MAX_RANGE)
            new_car.setposition(x=300, y=y_position)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.forward(self.speed)
            if car.xcor() == -300:
                car.reset()
                car.color("white")
                self.car_list.remove(car)
