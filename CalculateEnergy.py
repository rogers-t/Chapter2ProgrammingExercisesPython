# How to calculate energy

waterWeight = eval(input("Enter the amount of water in kilograms: "))
initialTemperature = eval(input("Enter the initial temperature: "))
finalTemperature = eval(input("Enter the final temperature: "))

energy = waterWeight * (finalTemperature - initialTemperature) * 4184

print("The energy needed is", energy)