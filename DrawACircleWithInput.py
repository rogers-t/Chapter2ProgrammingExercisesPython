# How to draw circle with input from the user in turtle and display the area

from math import pi
import turtle

centerX, centerY = eval(input("Enter the center of the circle (x,y): "))
radius = eval(input("Enter the radius of the cirlce: "))
area = pi * (radius * radius)

turtle.penup()
turtle.goto(centerX, centerY)
turtle.write(round(area, 2))
turtle.right(90)
turtle.forward(radius)
turtle.left(90)
turtle.pendown()
turtle.circle(radius)

turtle.done()