from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Data.txt", mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(-180, 270)
        self.write(f"SCORE: {self.score}", align='right', font=FONT)
        self.goto(100, 270)
        self.write(f"HIGH SCORE: {self.highscore}", align='left', font=FONT)

    def update_score(self):
        self.score += 10
        self.update_display()
