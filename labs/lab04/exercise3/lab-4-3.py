hours = int(input())
if hours > 2:
    if hours > 5:
        fee = 3
    else:
        fee = 2
else:
    fee = 0
parkingFee = hours * fee
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)
