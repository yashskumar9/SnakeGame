from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=600, height=600)
my_screen.title('Snake Game')
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(key='Up', fun=snake.move_up)
my_screen.onkey(key='Down', fun=snake.move_down)
my_screen.onkey(key='Left', fun=snake.move_left)
my_screen.onkey(key='Right', fun=snake.move_right)
my_screen.onkey(key='Right', fun=snake.move_right)

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with walls
    if snake.is_collide():
        score.game_over()
        snake.reset()
        score.reset()

    # snake meets the food
    if snake.head.distance(food) < 15:
        food.update_food()
        snake.update_snake()
        score.update_score()

my_screen.exitonclick()
