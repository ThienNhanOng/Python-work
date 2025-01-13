# this lesson will go over what a collection is. a collection is a single "variable" that is used to store multiple values
#notes of different kinds of collections  
    #   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
    # [] index operator [start: end : step]
    
vehicles = ("car", "truck" , "plane" , "train" , "train")
#print(dir(vehicles))
#print(help(vehicles))
#print(len(vehicles))
#print("pineapples" in vehicles)
print(vehicles.index("truck"))
print(vehicles.count("train"))
#vehicles.add("pineapples")
#vehicles.remove("car")
#vehicles.pop() #remove the first element at random
#vehicles.clear()

print(vehicles)