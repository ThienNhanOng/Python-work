#this will generate random numbers

import random

#print(help(random)) #remove the # to learn the different functions for the import random

low = 1
high = 100
options = ("rock", "paper", "scissors")

number = random.randint(low,high)
number = random.random()
option = random.choice(options)

print(number)
print(option)