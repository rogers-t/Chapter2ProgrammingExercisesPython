# How to calculate runway length

speed, acceleration = eval(input("Enter speed and acceleration: "))

length = pow(speed, 2) / (2 * acceleration)

print("The minimum runway length for this airplane is", round(length,3), "meters")