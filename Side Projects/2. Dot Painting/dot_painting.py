import turtle as t
import random
turtle = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle.hideturtle()
turtle.speed(10)
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(colours))
    turtle.forward(50)

    if dot_count%10==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

t.exitonclick()