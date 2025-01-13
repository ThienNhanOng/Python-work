# this lesson will go over what a collection is. a collection is a single "variable" that is used to store multiple values
#notes of different kinds of collections
    #   List  = [] ordered and changeable. Duplicates OK
    
    #this will go over what a list is.
    
    #       take the # out of the print below for example 
    #(print(dir(fruit))) all type of methods this list can preform
    # https://www.youtube.com/watch?v=gOMW_n2-2Mw&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=21  
#list example
fruit = ["apple", "orange" , "coconut" , "banana"] 
# apple = 0 orange = 1 coconut = 2 banana = 3
print(fruit[0:2]) #changing this index operator allow you to choose which fruit

#fruit[0] = "pineapple" # this will resign the apple to a pineapple
#fruit.append("pineapples") 
fruit.remove("apple") #this will remove an apple
#fruit.insert(0, "meat") #this will insert a food.
fruit.sort() # this will make the list alphabetical order. 
#fruit.reserse()
#fruit.clear()

for fruit in fruit:
    print(fruit)

