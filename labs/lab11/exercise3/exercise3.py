number = int(input())
count=0
biggest_jump=0
previous_num=number

while number !=0:
    jump=number-previous_num
    if jump > biggest_jump:
      biggest_jump=jump
    previous_num=number
    count+=1
    number = int(input())
    


print(count)
print(biggest_jump)
