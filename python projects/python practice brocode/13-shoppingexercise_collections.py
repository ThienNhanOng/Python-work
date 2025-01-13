#this exercise will practice lists sets and tuples 
# in this program there will be two lists foods and prices

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy or click q to quit ")
    if food.lower() == "q":
        break 
    else: 
        price = float(input(f"enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("~~~~~~YOUR CART~~~~~~")

for food in foods:
    print(food,end=" ")

for price in prices:
    total += price
print()
print(f"your total is: ${total}")