from turtle import Turtle
FONT = ("Courier", 24, "normal")


# Keeps track of the score
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.move_speed = 0.1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score + 1}", align="center", font=FONT)

    def track_score(self):
        self.score += 1
        self.move_speed *= 0.75
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
