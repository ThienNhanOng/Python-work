#in this exercise we will import the built in math function in python.
#this will allow us to access rounding a number up and down, and squaring a number.
# as well as have access to valued numbers such as pi (3.14) and e (exponential constant)
#----- code below

import math 
defaultnumber = 10.4
# provide the pi and e value without manually giving it a value
print( "pi number is " + str(math.pi))
print("exponential constant number is " + str(math.e))
# square root a number
squrerootnumber = str(math.sqrt(defaultnumber))
print( "the square root of 10 is = " + squrerootnumber)

# this exercise below will round a number up and down
# round up
roundupnumber = math.ceil(defaultnumber)
print(roundupnumber)
# round down
rounddownnumber = math.floor(defaultnumber)
print(rounddownnumber)