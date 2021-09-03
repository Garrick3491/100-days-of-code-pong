from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Padel(Turtle):
    def __init__(self, starting_x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fast")
        self.goto((starting_x, 0))
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)