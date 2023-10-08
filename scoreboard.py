from turtle import Turtle

FONT = ("Arial", 14, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("data.txt", mode="r")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = -1
        # self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 14, 'normal'))
        self.score_up()

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.home()
    #     self.write(arg=f"Game Over\n Your score: {self.score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", mode="w")
            file.write(f"{self.high_score}")
            self.score = -1
            self.score_up()

