from turtle import Turtle, up

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):
    self.snake_body = []
    self.create_snake()
    self.head = self.snake_body[0]
    self.direction = self.head.heading()

  def create_snake(self):
    for position in STARTING_POSITION:
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.snake_body.append(new_segment)

  def move(self):
    for seg_num in range(len(self.snake_body) - 1, 0, -1):
      new_x = self.snake_body[seg_num - 1].xcor()
      new_y = self.snake_body[seg_num - 1].ycor()
      self.snake_body[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.direction != DOWN:
      self.head.setheading(UP)  

  def down(self):
    if self.direction != UP:
      self.head.setheading(DOWN)  

  def left(self):
    if self.direction != RIGHT:
      self.head.setheading(LEFT)  

  def right(self):
    if self.direction != LEFT:
      self.head.setheading(RIGHT)