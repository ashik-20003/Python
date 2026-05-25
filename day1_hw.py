import random

rice_price = 45
rice_quantity = 3

sugar_price = 40
sugar_quantity = 2.5

oil_price = 130
oil_quantity = 1.8

rice_total = rice_price*rice_quantity
sugar_total = sugar_price*sugar_quantity
oil_total = oil_price*oil_quantity

print("Total price for rice is ",rice_total)
print("Total price for sugar is ",sugar_total)
print("Total price for oil is ",oil_total)

total_bill = rice_total + sugar_total + oil_total
print("Total bill as integer : ",int(total_bill))
print("Total bill as string : ",str(total_bill))

total_with_delivery = total_bill + random.randrange(5,10)
print("The total with delivery is ", total_with_delivery)
