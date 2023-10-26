from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1_score = 0

    def setup(self):
        self.clear()
        self.setpos(-295, 260)
        self.write(f"Current level \n{self.player_1_score}", False, "left", FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", ("Courier", 25, "bold"))