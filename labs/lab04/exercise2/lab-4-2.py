income = float(input())
if income > 50000:
    if income > 100000:
        tax = 0.02
    else:
        tax = 0.01
else:
    tax = 0
totalTax = tax * income
print(totalTax)
