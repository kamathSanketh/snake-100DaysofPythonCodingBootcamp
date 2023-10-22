from turtle import Turtle

class ScoreBoard(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("valStorage.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write("Score: " + str(self.score) + " High Score: " + str(self.high_score), align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        self.score = self.score + 1
        self.write("Score: " + str(self.score) + " High Score: " + str(self.high_score), align="center", font=("Arial", 24, "normal"))
     # def end_game(self):
        # self.clear()
        # self.goto(0, 0)
        # self.write("Game Over", align="center", font=("Arial", 60, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("valStorage.txt", mode="w") as file:
                file.write(str(self.score))

        self.score = 0
        self.update_score()
