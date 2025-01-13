# an if statement is to do some code only if the conditions has been met or is true.

#exercise ask for users age
age = int(input("Enter your age: "))

if age >= 100:
    print("you are too old to sign up go fuck yourself")
elif age >= 18:
    print("you are now signed up")
elif age <= 0:
    print("you cannot make an account for an unborn child")
else:
    print("u are too young to sign up sign up")

