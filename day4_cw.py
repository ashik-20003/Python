fruits = ["apple","orange","banana"]
vegetables = ["Potato","Carrot","Onion"]
beverages = ["Pepsi","7UP","Cola"]

fruits.append("Cherry")
vegetables.insert(1,"Cucumber")
beverages.pop()
inventory = fruits + vegetables + beverages
print("First 2 fruits : ",fruits[:2])
print("Last item from vegetables : ",vegetables[-1])
fruits_length = [len(x) for x in fruits]
water_in_beverages = "Water" in beverages
first_item = (fruits[0],vegetables[0],beverages[0])