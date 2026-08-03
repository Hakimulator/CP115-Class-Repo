import random
class_name=input("Enter class name (comas separated):")
today_class= class_name.split(",")
today_class= random.choice(today_class)
print(f"Class of the day is {today_class}")