MAUREEN NYAGA #SCT21-0052/2022
print("Hello")
#prompt user for input
UserMass=input("Please enter your mass in kg ")
UserHeight=input("Please enter your height in meters ")
UserMass=float(UserMass)
UserHeight=float(UserHeight)
HeightSquared=UserHeight*UserHeight
#calculate BMI
BMI=UserMass/HeightSquared
if (BMI<18.5):
    print("Underweight")
elif (BMI>24.9):
    print("Overweight")
else: print("Normal")
