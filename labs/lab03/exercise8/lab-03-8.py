principal = float(input())
rate = float(input())
time = float(input())
interest = principal * rate * time / 100
totalAmount = principal + interest
monthlyInterest = interest / time * 12
print(interest)
print(totalAmount)
print(monthlyInterest)
