item=input("Enter item name:")
price=float(input("Enter item price:"))
quantity=3
tax=0.06
subtotal= price*quantity
tax_amount= subtotal*tax
total_cost= subtotal+tax_amount 
print(f"Subtotal: RM{subtotal}")
print(f"Tax amount:RM{tax_amount}")
print(f"Total cost: RM{total_cost}")