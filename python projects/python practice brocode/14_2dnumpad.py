#2d tupple numpad exercise
#this exercise will create a phone numpad and show an example of it.
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0 , "#"))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()
    
board = ( 
         ["x","x","x"]
         )