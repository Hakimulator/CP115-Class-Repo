number = int(input())
score = 0
highest = 0
ignored = 0

while number !=0:
    number = int(input())
    if number > score:
        score += number
        highest = number
        continue
    ignored +=1


print(score)
print(ignored)
