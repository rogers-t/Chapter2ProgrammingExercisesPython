# How to draw four circles with input from user

import turtle

radius = eval(input("Enter the radius for the circles: "))

turtle.circle(radius)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.circle(radius)

turtle.done()