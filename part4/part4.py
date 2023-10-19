from turtle import Screen
from part4.snake_part4 import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

screen.update()

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.5)

  snake.move()

screen.exitonclick()
