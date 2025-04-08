from turtle import Turtle,Screen
import time
positions=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.screen=Screen()
        self.segments=[]
        for i in range(3):
            new_seg=Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(positions[i])
            self.segments.append(new_seg)
        self.head=self.segments[0]
    def move(self):
        self.screen.listen()
        def turn_right():
            if self.head.heading() != 180:
                self.head.setheading(0)
        def turn_left():
            if self.head.heading() != 0:
                self.head.setheading(180)
        def turn_down():
            if self.head.heading() != 90:
                self.head.setheading(270)
        def turn_up():
            if self.head.heading() != 270:
                self.head.setheading(90)
        for i in range(len(self.segments)-1,0,-1):
            x_cord=self.segments[i-1].xcor()
            y_cord=self.segments[i-1].ycor()
            self.segments[i].goto(x_cord,y_cord)     
        self.head.forward(20)
        self.screen.onkey(turn_right,"d")
        self.screen.onkey(turn_left,"a")
        self.screen.onkey(turn_up,"w")
        self.screen.onkey(turn_down,"s")
    def add_body(self):
        new_seg=Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        self.segments.append(new_seg)


        
