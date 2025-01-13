#these are practice exercises done for if, else if and else problems. 

response = input("would you like food? (Y/N)")
if response == "Y" or "y":
    print("i made some pizza for you!")
else: 
    print("no food for you")
    
    
    
name = input ("enter your name ")
if name == "":
    print("YOU DID NOT ENTER YOUR NAME")
else:
    print("hello " + name)
    
    
    
online = False
if online: 
    print("the computer is online")
else:
    print("the user is offline")