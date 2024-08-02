from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-250, 250)
        self.update_scoreboard()

    def increase(self):
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level : {self.level}", font=FONT)

    def game_over(self):
        self.write(arg=f"GAME OVER", align="center", font=FONT)
