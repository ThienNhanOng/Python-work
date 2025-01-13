#indexing allow access to elements of a sequence using [] (index operator)
# index number start at 0. there are 3 steps. [start, end, step]. 

credit_number = "1234-5678-9012-3456"
print(credit_number[1]) # print the 2nd number
print(credit_number[0:4]) # print the first 4 number
print(credit_number[5:9]) # print the second set of numbers
print(credit_number[5:]) # print the second set of numbers all the way to the end
print(credit_number[-1]) # count backwards [6]
print(credit_number[-4]) # count backwards [3]

last_digit = credit_number[-4:] #count backwards and show the remaining set
print(last_digit) # show the last 4 digits 
