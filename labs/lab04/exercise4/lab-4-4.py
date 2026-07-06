weight = int(input())
ticketPrice = int(input())
if weight > 0:
    if weight > 15:
        charge = weight - 15 * 4
    else:
        charge = 0
else:
    charge = -10
finalPrice = ticketPrice + charge
print(finalPrice)
