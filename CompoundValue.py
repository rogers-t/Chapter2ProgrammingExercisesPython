# How to compound value

monthlySavingAmount = eval(input("Enter the monthly saving amount: "))

annualInterestRate = 0.05
monthlyInterestRate = annualInterestRate / 12

firstMonthValue = monthlySavingAmount * (1 + monthlyInterestRate)
secondMonthValue = (monthlySavingAmount + firstMonthValue) * (1 + monthlyInterestRate)
thirdMonthValue = (monthlySavingAmount + secondMonthValue) * (1 + monthlyInterestRate)
fourthMonthValue = (monthlySavingAmount + thirdMonthValue) * (1 + monthlyInterestRate)
fifthMonthValue = (monthlySavingAmount + fourthMonthValue) * (1 + monthlyInterestRate)
sixthMonthValue = (monthlySavingAmount + fifthMonthValue) * (1 + monthlyInterestRate)

print("After the sixth month, the account value is", round(sixthMonthValue, 2))