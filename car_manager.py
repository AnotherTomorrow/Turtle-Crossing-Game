from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # Initializes the objects
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.penup()
        self.hideturtle()

    # Generates 1-6 new cars randomly on the Y-coordinate and adds them to the list initialized in the object.
    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            rand_ycor = random.randint(-250, 250)
            new_car.goto(310, rand_ycor)
            self.all_cars.append(new_car)

    # All cars in all_cars list are prompted to move backwards because they start on the right side of the screen.
    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
