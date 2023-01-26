# How to calculate BMI

weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

weightKilograms = weight * 0.45359237
heightMeters = height * 0.0254

bmi = weightKilograms / pow(heightMeters, 2)

print("BMI is", round(bmi, 4))