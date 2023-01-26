# How to calculate future investment value

investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = (annualInterestRate / 100) / 12
numberOfMonths = numberOfYears * 12

futureInvestmentValue = investmentAmount * pow(1 + monthlyInterestRate, numberOfMonths)

print("Accumulated value is", round(futureInvestmentValue, 2))