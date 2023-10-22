from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
    def createSnake(self):
        for x in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            temp = 0 - (x * 20)
            t.goto(temp, y=0)
            self.segments.append(t)
    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            tempX = self.segments[x - 1].xcor()
            tempY = self.segments[x - 1].ycor()
            self.segments[x].goto(tempX, tempY)
        self.segments[0].fd(MOVE_DISTANCE)
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def addPiece(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        temp = len(self.segments)-1
        newX = self.segments[temp].xcor() -20
        newY = self.segments[temp].ycor()
        t.goto(newX, newY)
        self.segments.append(t)
    def check_for_wall_hit(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        else:
            return False

    def check_for_snake_hit(self):
        for i in range(2, len(self.segments)):
            if self.head.distance(self.segments[i]) < 5:
                return True

        return False

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]