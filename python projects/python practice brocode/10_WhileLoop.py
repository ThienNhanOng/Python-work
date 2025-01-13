# a while loop will execute while some condition remains true. 

name = (input("enter your name: "))
while name =="":
    print("you did not enter your name.")
    name = (input("Enter your name:"))
          
age = int(input("enter your age: "))
while age < 0:
    print("you did not enter your age.")
    age = int(input("Enter your age:"))
print(f"hello {name}, you are {age} years old")

#exercise 3
food = input("what is your favorite food? (q to quit)")
while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit)")
print("bye")

 