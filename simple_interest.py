#WAP to calculate simple interest.
'''
Formula SI = (P * R * T) / 100
P - Principal amount(Rs)
R - Rate of interest(%)
T - Time(yrs / Months)

Lets take P - 1000rs R - 5% T - 1year
'''

#Input values for Simple Interest.
Principal = float(input("Enter the principal amount: "))
Rate = int(input("Enter the rate: "))
Time = int(input("Enter the time: "))

#Calculation
Simple_Interest = (Principal * Rate * Time) / 100
print(f"The Simple Interest for a principal of {Principal} at a rate of {Rate}% over {Time} years is: {Simple_Interest}Rs")
