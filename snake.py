from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(0,-20),(0,-40)]
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            x_new = self.snake[seg - 1].xcor()
            y_new = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)
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
    def add_segment(self,position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.snake.append(new)
    def extend(self):
        self.add_segment(self.snake[-1].position())



