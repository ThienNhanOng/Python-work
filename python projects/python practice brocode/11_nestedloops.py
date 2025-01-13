#nested loops are a loop inside of another loop (outer,inner)
# this is a normal four loop
for x in range (1,10):
    print(x, end ="")
    
print("next exercise")

#this will reprint the exercise above 3 times a loop inside a loop!
for y in range(3):
    for y in range (1,10):
        print(y, end = "")
    print() # this will add a space in between every print
    
print("next exercise")

#this exercise allow user to input the symbol to create a rectangle     
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = (input("enter the number of symbols: "))

for x in range(rows):
    for y in range (columns):
        print(symbol, end="")
    print()