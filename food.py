from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('light blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.update_food()

    def update_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
