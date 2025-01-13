# This lesson will go over what a variable is and how to check and change the data type as well as combine two of the same data type. 



# A variable is a container for a value. it behaves as the value that it contains
# this exercise will set the variable name and give it the string value "bro" then it will print to the console
# by putting the 'type' before the variable "name" it will print the type of variable it is. in this case it is a "STRING"

name = "Bro"
print(name)
print(type(name))
#the result is "bro" and 'str' printed to the console.
#-------------------------------------------
#part 2 of variables. this lesson will show you how to connect 2 variables of the SAME DATA TYPE
#this exercise set a variable for the first name and last name and combine to give a value to the "full name" variable
first_name ="Thien"
last_name = " Ong"
full_name = first_name+last_name

print("hello " + full_name)
#----------------------------------
#variable part 3. this exercise teaches how to use integer variables
age = 21
age += 1
print(age) #note: if you want to do 'your age is: age' it will not work without TYPECASTING

#variable part 4: how to typecast age so you can use a string variable
#this exercise show how to typecast by changing the integer (ages) and changing it into a string (str)
ages = age
print("your age is " + str(ages))