#this else if exercise allow the user to input a temp and conver it. 
# this exercise help grasp the idea of if statements 

unit = input("is this temperature in celsius or fahrenheit (C/F)")
temp = float(input("enter the temperature"))

if unit == "C" or "c":
    temp = round((9 * temp) / 5 + 32 , 1)
    print(f"the temperature in fahrenheight is: {temp} F" )
elif unit == "F" or "f":
    temp = round((temp - 32) * 5 / 9,1)
    print(f"the temperature in celsius is {temp} C" )
else: 
    print(f"{unit} is an invalid unit of measurement")