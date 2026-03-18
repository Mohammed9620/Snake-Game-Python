from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")
score=0

class Score(Turtle):
    def __init__(self):
        super().__init__()
        #Read the highest score
        with open("data.txt", mode="r") as data:
            self.highest_score = int(data.read())
        self.score=0
        self.color("White")
        self.penup()
        self.goto(x=0,y=260)
        self.hideturtle()
        self.update_record()
    def update_record(self):
        self.clear()
        self.write(arg=f"Score {self.score}:",align=ALIGNMENT,font=FONT)
        if self.score>self.highest_score:
            self.highest_score=self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highest_score}")
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_record()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over",align=ALIGNMENT,font=FONT)
        self.goto(x=-90,y=-20)
        self.write(arg=f"Highest Score:{self.highest_score}", font=FONT)


