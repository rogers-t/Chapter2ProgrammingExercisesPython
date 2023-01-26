# Calculate population projection with input of years from user

numberOfYears = eval(input("Enter the number of years: "))

currentPopulation = 312032486

births = (1 / 7) * 31536000
deaths = (1 / 13) * 31536000
immigrants = (1 / 45) * 31536000

populationChange = round(births - deaths + immigrants)

population = currentPopulation + (populationChange * numberOfYears)

print("The population in", numberOfYears, "is", round(population, 0))

