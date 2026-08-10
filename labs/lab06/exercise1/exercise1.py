item1 = "Coffee"
price1 = 3.50
quantity1 = 2

item2 = "Muffin"
price2 = 2.10
quantity2 = 3

item3 = "water"
price3 = 1.05
quantity3 = 4

total1= price1*quantity1
total2= price2*quantity2
total3= price3*quantity3

subtotal= total1+total2+total3
tax= subtotal*0.06
total=subtotal+tax

print (
    f"========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\n{item1}\t{price1}\t{quantity1}\t{total1}\n{item2}\t{price2}\t{quantity2}\t{total2}\n{item3}\t{price3}\t{quantity3}\t{total3}\n------------------------------\nSubtotal\t\t${subtotal}\nTax(6%)\t\t\t${tax}\nTotal\t\t{total}\n============================")