# How to split digits

integer = eval(input("Enter an integer: "))

digit1 = integer // 1000
currentInteger = integer % 1000
digit2 = currentInteger // 100
currentInteger = currentInteger % 100
digit3 = currentInteger // 10
digit4 = currentInteger % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)
