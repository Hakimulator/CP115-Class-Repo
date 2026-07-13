gb = int(input())
if gb >= 20:
    gb = gb - 20
    bill = 3 * gb + 25
else:
    bill = gb + 10
print(bill)
