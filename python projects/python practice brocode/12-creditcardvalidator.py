#python credit card validator program exercise
#this exercise will practice the loops in lesson 10-12

#this exercise will remove any dashes that the user may of entered in.
# this will add all digits in the odd places from right to left
# this will double every second digit number
# if its a 2 digit number, add them together to get a single digit.
# sum of all digits


sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step 1:
card_number = input("Enter a credit card number ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1] #this will reverse the card number 

# step 2:
for x in card_number[::2]:
    sum_odd_digits += int(x)
    
#step 3: double every digit from right to left
for x in card_number[1::2]: #start at the second digit which has an index of 1
    x = int(x) * 2
    if x >= 10: 
        sum_even_digits += (1+(x % 10))
    else:
        sum_even_digits += x
        
#step 4: add the sum of even and odd digits
total = sum_odd_digits + sum_even_digits

#step 5:
if total % 10 == 0:
    print("valid")
else:
    print("invalid")

