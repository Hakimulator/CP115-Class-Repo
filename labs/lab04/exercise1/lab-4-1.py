kwh = int(input())
if kwh >= 100:
    if kwh > 200:
        charges = 0.75
    else:
        charges = 0.5
else:
    charges = 0.3
totalBill = kwh * charges
print(totalBill)
