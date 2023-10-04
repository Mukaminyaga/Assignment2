print("Hello")
#prompt user for input
Year=input("Please enter the year: ")
Year=int(Year)
#check if it's a leap year
if (Year%4==0)and(Year%100!=0):
    print("Leap Year")
elif(Year%400==0):
    print("Leap Year")
else: print("Not a leap year")
