minutes = int(input())
total_minutes= minutes 
customers = 1

while total_minutes < 60:
    minutes = int(input())
    if total_minutes+minutes>60:
        total_minutes += minutes
        customers +=1
        break
    total_minutes += minutes
    customers +=1
    


print(customers)
print(total_minutes)
