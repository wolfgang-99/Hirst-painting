# with this program you can extract color from any pics of your choice once you save the pic in this folder
import turtle
import random
from colorgram import extract
from turtle import Screen, Turtle

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.shape("turtle")
tim.speed("fastest")
color = extract("image_color.jpeg", 30)
turtle.colormode(255)
list_color = []


def extract_color(amount):
    for no_color in range(0, amount):
        colors = color[no_color]
        rgb_color = colors.rgb
        print(rgb_color)
        list_color.append(rgb_color)


extract_color(10)

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100
for dot_count in range(1, number_of_dot+1):
    color_extracted = random.choice(list_color)
    tim.dot(20, color_extracted)
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
