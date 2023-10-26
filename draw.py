from turtle import Turtle


class Draw(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("DarkGreen")
        self.pensize(3)

    def draw_lines(self):
        self.penup()
        self.setpos(300, -250)
        self.seth(180)
        self.pendown()
        self.forward(600)
        self.penup()
        self.setpos(300, 250)
        self.pendown()
        self.forward(600)

