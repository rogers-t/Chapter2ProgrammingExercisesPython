# How to calculate an area of a hexagon

from math import sqrt


side = eval(input("Enter the side: "))

area = ((3 * sqrt(3)) / 2) * pow(side, 2)

print("The area of the hexagon is", round(area, 4))