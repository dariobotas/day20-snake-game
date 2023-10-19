from turtle import Screen, Turtle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")

#1st part
snake_body = []

for turtle in range(0,3):
  new_turtle = Turtle("square")
  new_turtle.color("white")
  new_turtle.penup()
  if turtle == 0:
    new_turtle.goto(x=0,y=0)
  else:
    new_turtle.goto(x=snake_body[turtle - 1].xcor()-20,y=0)
  snake_body.append(new_turtle)

#


screen.exitonclick()