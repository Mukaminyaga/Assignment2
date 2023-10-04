# MAUREEN NYAGA SCT211-0052/2022
print("Hello")
#prompt user to enter the values
BillAmount=input("Please enter the total bill amount: ")
Tipnumber=input("Please enter the amount you would like to tip(10%,12%,or15%): ")
NumberOfPeople=input("Please enter the number of people splitting the bill: ")
BillAmount=float(BillAmount)
Tipnumber=int(Tipnumber)
NumberOfPeople=int(NumberOfPeople)
TipAmount=float(BillAmount)*float(Tipnumber/100)
#calculate the totalbill
TotalBill=BillAmount+TipAmount
AmountToPay=TotalBill/NumberOfPeople
#use 2 decimal places
Amount=round(AmountToPay,2)
print("The amount each person should pay is: "+str(Amount))
