name = str(input("Enter employee's name: "))
hours = eval(input("Enter number of hours worked in a week: "))
pay = eval(input("Enter hourly pay rate: "))
fedRate = eval(input("Enter federal tax withholding rate: "))
stateRate = eval(input("Enter state tax withholding rate: "))

grossPay = float(format(pay * hours, ".2f"))
fedTax = float(format(fedRate * grossPay, ".2f"))
stateTax = float(format(stateRate * grossPay, ".2f"))
deduction = float(format(fedTax + stateTax, ".2f"))
netPay = float(format(grossPay - deduction, ".2f"))

print("\nEmployee name:", name, 
	"\nHours Worked:", format(hours,".1f"),
	"\nPay Rate:", '${}'.format(pay),
	"\nGross Pay:", '${}'.format(grossPay),
	"\nDeductions:",
	"\n  Federal Withholding", "(" + format(fedRate,".1%") + "):", '${}'.format(fedTax),
	"\n  State Withholding", "(" + format(stateRate,".1%") + "):", '${}'.format(stateTax),
	"\n  Total Deduction:", '${}'.format(deduction),
	"\nNet Pay:", '${}'.format(netPay))
