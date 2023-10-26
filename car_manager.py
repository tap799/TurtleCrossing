import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE
        # self.shape("square")
        # self.shapesize(.8, 2)
        # self.penup()
        # self.color(random.choice(COLORS))
        # self.setx(280)

    def create_cars(self):
        # all_ys = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120,
        # 140, 160, 180, 200, 220, 240, ] chosen_positions = []
        random_chance = random.randint(1,6)
        if random_chance == 6:
            car = Turtle("square")
            car.shapesize(.8, 2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.uniform(-250, 250)
            random_x = random.uniform(300, 325)
            car.setx(random_x)
            car.sety(random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
