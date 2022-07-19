# Creating a program that allows user to enter name and cost of an expense
# 07/18/2022
# CTI-110P1HW2 - BBasic Math
# Clarissa Isom-Rodriguez
#

nmExp = input("Enter name of expense: ")
mnCharge = input("Enter monthly charge: ")

monthly_tax=float(mnCharge)*(0.06)
monthly_charge= float(float(monthly_tax) + float(mnCharge))
annual=float(float(monthly_charge)*12)

print("Bill: "+str(nmExp)+" --------- Before Tax: $"+format(float(mnCharge),".2f"))
print("Monthly Tax: $"+format(monthly_tax,".2f"))
print("Monthly Charge: $"+format(monthly_charge,".2f"))
print("Annual Charge: $"+format(annual,".2f"))
