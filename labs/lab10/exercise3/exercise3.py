target_points = int(input())

total_points=0
rounds_played=0
point=0
while target_points>total_points:
    point=int(input())
    rounds_played+=1
    total_points+=point

print(total_points)
print(rounds_played)
