#a 2d list is a list made within a list (like a excel spreadsheet)
#this lesson will make a list with fruits, vegetables, and meat

#this is a 1D list
fruits = [   "apples" , "oranges" , "bananas" , "coconut" ]
vegetables = ["celery" , "carrots" , "potatos"]
meats = [    "chicken" , "beef" , "pork"]

groceries = [fruits,vegetables,meats]
print(groceries[0][1]) #this make oranges
print(groceries[2][1]) #beef
print(groceries[1][1]) #carrots

for collection in groceries:
    for food in collection:
        print(collection)
    print(food)