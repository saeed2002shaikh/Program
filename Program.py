p = float(input("Enter principal amount: "))
R = float(input("Enter  Interest Rate
 "))
n = int(input("Enter Tenure " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)

print("Monthly EMI = ", emi)
