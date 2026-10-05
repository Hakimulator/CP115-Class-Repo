a = int(input())
b = int(input())
overtake_round = 0
round=0
while a != -1 :
    a = int(input())
    b = int(input())
    if b>a:
        overtake_round=round+1
        break
    round+=1
    


print(overtake_round)
