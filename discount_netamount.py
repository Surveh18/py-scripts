# Program to calculate discount and net amount

#Input the billing amount
billing_amount = int(input("Enter the billing amount: "))

# Calculating the discount (5%)
discount = (5 / 100) * billing_amount

#Calculating the net amount after discount
net_amount = billing_amount - discount

#Display of discount and net amount
print(f"Billing Amount: {billing_amount}")
print(f"Discount (5%): {discount}")
print(f"Net Amount after Discount: {net_amount}")
