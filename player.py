from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.setpos(STARTING_POSITION)
        self.seth(90)

    def move_up(self):
        self.seth(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.seth(270)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.seth(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.seth(0)
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.setpos(STARTING_POSITION)
        self.seth(90)
