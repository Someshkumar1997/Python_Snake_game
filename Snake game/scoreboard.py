from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score {self.score}", False, align= ALIGN, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align= ALIGN, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()