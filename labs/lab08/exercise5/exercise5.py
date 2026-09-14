main_course = input()
drink = input()
dessert = input()

if main_course== "Chicken":
    price1= 10
elif main_course == "Beef":
    price1 = 12
else:
    price1 = 11
if drink == "Soft Drink":
    price2 = 2
else:
    price2 = 3
if dessert == "Ice Cream":
    price3=4
else:
    price3=5

service_charge= (price1+price2+price3)*0.1
final_bill= price1+price2+price3+service_charge

print(f"{final_bill:.2f}")
