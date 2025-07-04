from turtle import Turtle
POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.all_segment=[]
        self.create_snake()
        self.head=self.all_segment[0]

    def create_snake(self):
        for position in POS:
            self.add_segment(position)
    def add_segment(self, position):
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.goto(position)
        self.all_segment.append(segment)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for seg in range(2, 0, -1):
            new_x = self.all_segment[seg - 1].xcor()
            new_y = self.all_segment[seg - 1].ycor()
            self.all_segment[seg].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

