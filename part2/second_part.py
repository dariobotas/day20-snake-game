from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_position = [(0,0), (-20,0), (-40,0)]

snake_body = []

for position in starting_position:
  new_segment = Turtle("square")
  new_segment.color("white")
  new_segment.penup()
  new_segment.goto(position)
  snake_body.append(new_segment)

screen.update()

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.5)
  
  for seg_num in range(len(snake_body) - 1, 0, -1):
    new_x = snake_body[seg_num-1].xcor()
    new_y = snake_body[seg_num-1].ycor()
    snake_body[seg_num].goto(new_x, new_y)
  snake_body[0].forward(20)
    

screen.exitonclick()