# How to sum the digits in an integer

number = eval(input("Enter a number between 0 and 1000: "))

digit1 = number % 10
digit2 = number // 10 % 10
digit3 = number // 100 % 10

total = digit1 + digit2 + digit3

print("The sum of the digits is", total)