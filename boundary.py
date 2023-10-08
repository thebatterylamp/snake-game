from turtle import Turtle, Screen


def boundary():
    liner = Turtle("arrow")
    liner.hideturtle()
    liner.color("white")
    liner.penup()
    liner.goto(0, 290)
    liner.pendown()
    liner.forward(290)
    liner.right(90)
    liner.forward(580)
    liner.right(90)
    liner.forward(580)
    liner.right(90)
    liner.forward(580)
    liner.right(90)
    liner.forward(290)
