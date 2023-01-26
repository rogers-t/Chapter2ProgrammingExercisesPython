# How to calculate the number of years and days

minutes = eval(input("Enter the number of minutes: "))

years = minutes // 525600
days = minutes * (1 / 1440) % 365

print(minutes, "minutes is approximately", round(years), "years and", round(days), "days")