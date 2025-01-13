#this exercise allow the user to calculate the amount you are buying
item = input("what item would you like to buy? ")
price = float(input("what is the price? "))
quantity = float(input("how many are you buying? "))

total = price * quantity

print(f"you have bought {quantity} x {item}s")
print(f"your total is: ${round(total,2)}")