# Calculate investment amount

finalAccountValue = eval(input("Enter final account value: "))
annualInterestRate = eval(input("Enter annual interest rate in percent: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = (annualInterestRate / 100) / 12
numberOfMonths = numberOfYears * 12

initialDepositAmount = finalAccountValue / pow((1 + monthlyInterestRate), numberOfMonths)

print("Initial deposit value is", initialDepositAmount)