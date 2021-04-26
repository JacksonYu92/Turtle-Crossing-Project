from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.back_to_starting()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def back_to_starting(self):
        self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False