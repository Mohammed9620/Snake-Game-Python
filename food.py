from turtle import Turtle
import  random
shapes = ["arrow","turtle","circle","square","triangle","classic"]
colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "cyan", "magenta", "brown", "lime", "indigo",
    "violet", "gold", "coral", "salmon", "turquoise", "teal",
    "navy", "maroon", "olive", "peru", "orchid", "plum",
    "tomato", "crimson", "skyblue", "hotpink", "springgreen",
    "dodgerblue", "darkorange", "mediumvioletred", "chartreuse"
]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape()
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color()
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
