#learning about different string methods

name = input("enter your full name with dashes example: thien-nhan-ong : ")

# the length of the string (amount of characters)
result = len(name)
print(result)
# characters counted until e is found (example if type in (thiEn) there is 3
result2 = name.find ("e")
print(result2)

result3 = name.rfind("q")
print(result3)
# capitialize the first word
name4 = name.capitalize()
print(name4)
#cap all characters
name5=name.upper()
print(name5)
#make all characters lowercase
name6=name.lower()
print(name6)
#set true or false if all digits
name7=name.isdigit()
print(name7)
#set true if its all letters
name8=name.isalpha()
print(name8)

#count the dashes. (thien - nhan - ong has 2(-) dashes)
count = name.count("-")
print(count)        

#this will replace any dashes that was assigned in count with spaces
replace = name.replace("-", " ")
print(replace)