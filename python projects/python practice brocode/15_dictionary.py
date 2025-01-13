# a dictionary is a collection. {key:value} pairs
# it is ordered and changable and does not allow duplicates

capitals = {"usa": "washington D.C",
            "india"  : "New Delhi"  ,
            "China"  : "Beijing"    ,
            "Russia" : "moscow"    ,   
           }

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("japan"))

capitals.update({"germany" : "Berlin"})
capitals.update({"usa" : "detroit"})

if capitals.get("Russia"):
    print("that capital exists")
else: 
    print("that capital doesn't exist")

    
keys = capitals.keys()
for key in capitals.keys():
    print(key)

