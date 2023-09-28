# Ders 132,133

from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.body_olustur()
        self.head = self.parts[0]
        self.end = self.parts
        self.counter = 0

    def body_olustur(self):
        for position in positions:
            self.add_track(position)

    def add_track(self, position):
        body = Turtle(shape="square")
        body.color("green")
        body.penup()
        body.goto(position)
        self.parts.append(body)

    def enlarge(self):
        self.add_track(self.parts[-1].position())
        self.counter += 1

    def move(self):
        for element in range(len(self.parts) - 1, 0, -1):
            x = self.parts[element - 1].xcor()
            y = self.parts[element - 1].ycor()
            self.parts[element].goto(x, y)
        self.parts[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
