#input of customer information
customer_name = input("Enter customer name: ")
Product = input("Enter purchased product name: ")
Quantity = int(input("Enter the Quantity(no.s): "))
Rate_of_product = int(input("Enter the rate of product(Rs): "))
GST = int(input("Enter the GST(%): "))

#Display of Product purchased by user
print(f"Customer name = {customer_name}")
print(f"Purchased product = {Product}")
print(f"Product Qunatity = {Quantity}")
print(f"Rate of product = {Rate_of_product}")

#Calculation of bill
Amount = Quantity * Rate_of_product
print(f"Amount to be paid by the customer is {Amount}Rs.")

#Calculation of GST
GST_calc = (Amount * GST) / 100
print(f"GST amount is {GST_calc}%.")

#Toatal amount to be paid
Total = Amount + GST_calc
print(f"Total amount to be paid by customer is {Total}Rs.")
