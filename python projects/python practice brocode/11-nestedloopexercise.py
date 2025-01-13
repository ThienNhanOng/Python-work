#this exercise allow user to input the symbol to create a rectangle     
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = (input("enter the number of symbols: "))

for x in range(rows):
    for y in range (columns):
        print(symbol, end="")
    print()
    
