#this exercise create a program that converts weight kilograms to pounds 
# this exercise focus on if statements

weight = float(input("enter your weight: "))
unit = input ("kilograms or pounds? (p or k: )")

if unit == "P":
    weight = weight * 2.205
    unit = "LBS"
elif unit == "K":
    weight = weight / 2.205
    unit = "KGS"
else: 
    print(f"{unit} was not valid")
    
print(f"your weight is {weight} {unit}")