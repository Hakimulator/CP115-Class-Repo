scoreA = int(input())
scoreB = int(input())
if scoreA > scoreB:
    if scoreB > 0:
        pointsA = 3
    else:
        pointsA = 4
    pointsB = 0
else:
    if scoreA == scoreB:
        pointsA = 1
        pointsB = 1
    else:
        if scoreA > 0:
            pointsB = 3
        else:
            pointsB = 4
        pointsA = 0
print(pointsA)
print(pointsB)
