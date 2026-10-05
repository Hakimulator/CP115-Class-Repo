
correct_password = "python123"
login_successful = False
attempts_used = 0

for attempts_used in range (3):
    password = input()
    attempts_used +=1
    if password==correct_password:
        login_successful = True
        break
    
    
    


print(login_successful)
print(attempts_used)
