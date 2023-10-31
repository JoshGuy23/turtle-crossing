from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.print_level()

    def print_level(self):
        self.goto(x=-290, y=260)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def advance_level(self):
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
