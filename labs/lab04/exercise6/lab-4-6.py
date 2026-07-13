minutesBefore = int(input())
membership = (input().lower == 'true')
if minutesBefore > 30:
    price = 65
else:
    if minutesBefore > 0:
        price = 80
    else:
        price = 0
if membership:
    price = price * 0.85
print(price)
