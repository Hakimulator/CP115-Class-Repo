num_days = int(input())
danger_threshold = float(input())

danger_days=0
average_temp=0
total_temp=0
for running_days in range(1,num_days+1):
    days_temp = float(input())
    if days_temp>danger_threshold:
        danger_days += 1
    total_temp += days_temp
    average_temp=(total_temp)/running_days

print(danger_days)
print(f"{average_temp:.1f}")
