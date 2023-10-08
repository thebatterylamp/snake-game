from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.write(f" Score: {self.score}, Highest: {self.highest_score}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.clear()
        self.write(f" Score: {self.score}, Highest: {self.highest_score}", align="center",
                       font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()






