#math exercises using the import math function

import math

#this exercise will allow the user to input a value to calculate the circumfrence of a circle and round the number to the nearest th
radius = float(input("enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"the circumference is:  {round(circumference,3)}")
# method 2 of printing
print("the circumference is: " + str(circumference))

# this will calculate the area of a circle.
cirRadius = float(input("enter the radius of a circle"))
area = math.pi * pow(cirRadius,2)
print(f"the area of a circle is: {area}")
# method 2 of printing
print("the area of a circle is: " + str(area))

 # this exercuse will calculate the hypotenuse
sideA = float (input ("enter side a: "))
sideB = float (input ("enter side a: "))
c = math.sqrt(pow(sideA,2 + pow(sideB,2)))
print("result is " + str(c))