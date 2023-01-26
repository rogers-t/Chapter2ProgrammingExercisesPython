# How to calculate area of a triangle

from math import sqrt

x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

side1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
side2 = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
side3 = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))

s = (side1 + side2 + side3) / 2
area = sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is", round(area, 1))