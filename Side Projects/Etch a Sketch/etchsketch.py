from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()
arrow.setheading(90)


def move_forward():
    arrow.forward(10)


def move_backward():
    arrow.backward(10)


def turn_left():
    new_heading = arrow.heading() - 10
    arrow.setheading(new_heading)


def turn_right():
    new_heading = arrow.heading() + 10
    arrow.setheading(new_heading)


def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.setheading(90)
    arrow.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_left)
screen.onkey(key='a', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()