from turtle import Turtle , Screen
import random

screen = Screen()
game_is_on = False
screen.setup(width=500, height=400)
guess = screen.textinput(title="choose color", prompt="select the color")
colors=["red","blue","green","purple","cyan","grey"]
y_positions=[-180,-140,-110,-80,-50,-20]
turtle = []

for i in range(0,6):
  new_turtle = Turtle() 
  new_turtle.shape("turtle")
  new_turtle.penup()
  new_turtle.color(colors[i])
  new_turtle.goto(x=-220, y=y_positions[i])
  turtle.append(new_turtle)

if guess:
  game_is_on = True

while game_is_on:

  for i in turtle:

    if i.xcor() > 230:
      game_is_on = False
      winning_color = i.pencolor()
      if winning_color== guess:
        print(f"you have won and the winner is {winning_color}")
      else:
        print(f"you have lost and the winner is {winning_color}")

    distance = random.randint(0,10)
    i.forward(distance)





