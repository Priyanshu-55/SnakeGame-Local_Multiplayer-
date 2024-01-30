import turtle
DISTANCE = 40
# POSITION = [[0,0],[-20,0],[-40,0]]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self,color,POSITION):
        self.POSITION = POSITION
        self.colorseg = color
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for pos in self.POSITION:
            self.add_segment(pos)
    
    def add_segment(self,position):
            segment = turtle.Turtle()
            segment.penup()
            segment.shape('square')
            segment.shapesize(2)
            segment.color(self.colorseg)
            segment.goto(tuple(position))
            self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1 ].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto((new_x,new_y ))
        self.segments[0].forward(DISTANCE)
    
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