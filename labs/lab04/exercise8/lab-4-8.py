distance = float(input())
afterMidnight = (input().lower == 'true')
fare = 4 + 1.2 * (distance - 2)
if afterMidnight:
    fare = fare + 3
print(fare)
