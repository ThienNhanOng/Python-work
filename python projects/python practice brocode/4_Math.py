#this will demonstrate basic arithmetic operators
#------
#this operator will add 1 
addfriends = 5
addfriends = (addfriends) + 1
addfriends = str (addfriends) 
print("addition 5+1 = " + addfriends)

#this operator will subtract 1 
subtractfriends = 5
subtractfriends = (subtractfriends) - 1
subtractfriends = str (subtractfriends) 
print("subtract 5-1= " + subtractfriends)

#this operator will subtract 1 
subtractfriends = 5
subtractfriends = (subtractfriends) - 1
subtractfriends = str (subtractfriends) 
print("subtract 5-1= " + subtractfriends)

#this operator will DIVIDE 2 and implicit cast into a float 
dividefriends = 5
dividefriends = (dividefriends) /2 
dividefriends = str (dividefriends) 
print (f"division 5/2= " + dividefriends)

#this operator will raise by 2 
exponentfriends = 5
exponentfriends = (exponentfriends) ** 2
exponentfriends = str (exponentfriends) 
print ("exponent 5^2= " + exponentfriends)

#this operator will give the remainder of 2. 3+3+[2] = 8
remainderfriends = 8
remainderfriends = (remainderfriends) % 3
remainderfriends = str (remainderfriends) 
print ("remainder 8/3 = 2 with a remainer of = " + exponentfriends)
#----- Built in python mathematics functions
num1 = 3.14
num2 = 10
num3 = -5

#this operator will round the number. this exercise will change a float to an integer.
roundnum = num1
roundresult = round(roundnum)
print ("the number 3.14 will be rounded to = " + (str(roundresult)))

#this operator will give the absolute value of a number. absolute value are always positive
absolutevaluenum = num3
absolutevaluenumresult = abs(absolutevaluenum)
print ("this number will always be absolute meaning always positive. in this exercise -5 will always be = " + str (absolutevaluenumresult))

#this operator will raise a value 
powerresult = pow(num2,3)
print ("10 to the power of 3 = " + (str(powerresult)))

#this operator will give the highest value out of the given.
highresult = max(num1,num2,num3)
print ("the highest value between 3.14, 10, and -5 is = " + (str(highresult)))

#this operator will give the lowest value out of the given.
lowresult = min(num1,num2,num3)
print ("the lowest value between 3.14, 10, and -5 is = " + (str(lowresult)))