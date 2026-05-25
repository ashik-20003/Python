import random

apple_sold = 15.5
orange_sold = 20
grape_sold = 10.25

total_volume = apple_sold + orange_sold + grape_sold
print("The total volume sold is ",total_volume)

total_int = int(total_volume)
print("The total volume in int is ",total_int)

total_string = str(total_volume)
print("The total volume in string is ",total_string)

additional_litre = total_volume + random.randrange(5,10)
print("Total volume after additional litre is ",additional_litre)