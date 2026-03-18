import random
from turtle import  Turtle
from food import colors
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
            self.segments = []
            self.x = 0
            self.create_snake()
            self.head = self.segments[0]
    def create_snake(self):
        for position in range(3):
            self.add_segment()
    def add_segment(self, position=None):
        new_segment = Turtle(shape='square')
        new_segment.color(random.choice(colors))
        new_segment.penup()

        if position:
            new_segment.goto(position)
        else:
            new_segment.goto(x=self.x, y=0)
            self.x -= 20

        self.segments.append(new_segment)

    def extend_snake(self):
        # Pass the position of the very last segment to add_segment
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def control_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def control_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def control_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def control_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)