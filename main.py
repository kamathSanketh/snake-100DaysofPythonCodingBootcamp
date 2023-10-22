from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
segment = []
screen.tracer(0)

s = Snake()
food = Food()
scoreBoard = ScoreBoard()
screen.listen()
screen.onkey(s.Up, "Up")
screen.onkey(s.Down, "Down")
screen.onkey(s.Left, "Left")
screen.onkey(s.Right, "Right")

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(food) < 15:
        food.recool()
        s.addPiece()
        scoreBoard.update_score()
    if s.check_for_wall_hit() or s.check_for_snake_hit():
        scoreBoard.reset()
        s.reset()
screen.exitonclick()
