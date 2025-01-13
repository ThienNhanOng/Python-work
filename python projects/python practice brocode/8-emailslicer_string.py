#this exercise work string indexing. it takes your email and tell you what your 
#email username is and what your email domain is. example gmail.com or yahoo.com

email = (input("enter your email: "))

index = email.index("@")

username = email[:index] 
domain = email[index +1:]

print(f"your username is {username} and domain is {domain}")