# How to draw a rectangle with input from the user in turtle

import turtle

centerX, centerY = eval(input("Enter the center of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
height = eval(input("Enter the height of the rectangle: "))

turtle.penup()
turtle.goto(centerX, centerY)
turtle.goto((1 / 2) * centerX, (1 / 2) * centerY)
turtle.pendown()
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)

turtle.done()
