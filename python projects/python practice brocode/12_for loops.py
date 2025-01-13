# a for loop execute code for a fixed number of times example counting to 10

#this loop will print a number 1, and count up to 10
for x in range (1,11):
    print(x)

print("next")

#this loop will count down by 2 starting at 10
for y in reversed (range (1,11,2)):
    print(y)
    
print("next")

#this loop skips 13
for z in range (1,21):
    if z == 13: 
        break
    else: 
        print(z)