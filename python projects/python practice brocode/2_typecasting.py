#this lesson will go in depth for typecasting. type casting is a process of converting a value of one data type to another.
#this lesson will go through typecasting and how to convert explicitely vs implicitely. 
            #the different data types are (Strings) (integers) (float) (boolean)

#this exercise will demonstrate the 4 data types and print what kind they are in the console. 
Name = "thien"
age = 21
gpa = 3.9
student = True
print(type(Name))
print(type(age))
print(type(gpa))
print(type(student))
#   CONVERTING EXERCISES --------------------------------------
#this exercise will convert an INTEGER to a FLOAT.
age_float = age
age_float = float(age_float)
print(age_float) #this will print 21.0 instead of 21

#this exercise will convert a FLOAT to a INTEGER.
gpa_int = gpa
gpa_int = int(gpa_int)
print(gpa_int) #this will print 3 instead of 3.9

#this will convert a boolean into a string
student_bool = student
student_bool = str(student_bool)
print(type(student_bool)) #this will print "class str" if the type wasnt changed it would print "bool"

#converting a value into a boolean 
#if a boolean is anything other than '0' it is always set to true.
age_bool = 1
age_bool = bool(age_bool)
print(age_bool)

#converting a string into a boolean 
name_bool = "this has a name it is true" # this has characters filled so it is true
name_false = "" #this has nothing filled in so it is false
Nameresult = bool(name_false)
print(Nameresult) # this print either if the boolean is true or false

#implicit type casting is when the data value is converted automaticaly
x = 2
y = 2.0
x = x / y 
print(x) # x is converted automatically from a integer to a float. 