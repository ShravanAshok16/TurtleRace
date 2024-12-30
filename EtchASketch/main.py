from turtle import Turtle, Screen

t = Turtle()
def forwards():
    t.forward(10)

def backwards():
    t.backward(10)
    
def left():
    new_heading = t.heading()+10
    t.setheading(new_heading)
def right():
    new_heading = t.heading()-10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen = Screen()

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()