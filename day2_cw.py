receipt_header = '''MashupStack
Bookstore
'''
print(receipt_header)
title1 = "Python Basics"
title1_price = 450
title2 = "Data Science Intro"
title2_price = 600
title1_details = "Book Title : {0} - Price : {1}".format(title1,title1_price)
print(title1_details.upper())
title2_details = "Book Title : {0} - Price : {1}".format(title2,title2_price)
print(title2_details.upper())
total_amount = title1_price + title2_price
total_print = "Total Amount : {0} + {1} = {2}".format(title1_price,title2_price,total_amount)
print(total_print.upper())
print("THANK YOU FOR YOUR PURCHASE AT \n " + receipt_header.upper())