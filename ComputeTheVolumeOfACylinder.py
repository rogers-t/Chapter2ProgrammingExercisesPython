from cmath import pi

radius, length = eval(input("Enter the radius and length of a cylinder: "))

area = radius * radius * pi
volume = area * length

print("The area is", area)
print("The volume is", volume)