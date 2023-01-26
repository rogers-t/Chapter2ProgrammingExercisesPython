# How to calculate wind chill temperature

fahrenheit = eval(input("Enter the temperature in Fahrenheir between -58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))

windChill = 35.74 + (0.6215 * fahrenheit) - (35.75 * pow(windSpeed, 0.16)) + (0.4275 * fahrenheit * pow(windSpeed, 0.16))

print("The wind chill index is", windChill)