# Thien Ong / Alston Ni / Jacob Maunahan

"""
algorthim
main()
we made individual function: a function that displays the board, checks for wins, gets the player's move, checks for ties
1. print out the instruction for the game
2. asks players for their name
3. print out the board positioning for player reference
4. sets player1 as X and player2 as O
5. player1 starts first
6. displays empty board
7. the game will go on if no player wins or it is a tie
(these repeat)
8. get player1's move and put X it that board position
9. check for a win on the board
10. check for a tie
11. get player2's move and put O it that board position
12. checks for a win

individual functions:

displayboard function
1. displays the current board

win function
1. checks for 3 in a row of either X or O (horizontal)
2. checks for 3 in a row of either X or O (verticle)
3. checks for 3 in a row of either X or O (diagonal)

getmove function
1. each player takes turns inputting their move
2. makes each move is on the board
3. makes sure each position on the board can only have 1 symbol

tiegame function
1. check for any empty spots on the board

turtlehardprogramming function
1. draws what is in each spot of the board

"""

import turtle
#board = ["X","O","O","O","O","O","O","O","O"]


def turtlehardprogramming(t, screen, board):
    t = turtle
    s = screen
    b = board


    font_size = 50
    font = ("Arial", font_size, "normal")
    
    if board[0] == "X":     #if board position 1 is X, draws X
        t.penup()
        t.goto(-180, 100)
        t.pensize(10)
        t.write("X",font=font)
    elif board[0] == "O":   #if board position 1 is O, draws O
        t.penup()
        t.goto(-180,100)
        t.pensize(10)
        t.pendown()
        t.write("O", font=font)
    #repeats for each board position
    if board[1] == "X":
        t.penup()
        t.goto(-50,100)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[1] == "O":
        t.penup()
        t.goto(-50,100)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)

    if board[2] == "X":
        t.penup()
        t.goto(110,100)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[2] == "O":
        t.penup()
        t.goto(110,100)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)
        
    if board[3] == "X":
        t.penup()
        t.goto(-180, -10)
        t.pensize(10)
        t.write("X",font=font)
    elif board[3] == "O":
        t.penup()
        t.goto(-180, -10)
        t.pensize(10)
        t.write("O",font=font)
        
    if board[4] == "X":
        t.penup()
        t.goto(-50,-10)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[4] == "O":
        t.penup()
        t.goto(-50,-10)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)
        
    if board[5] == "X":
        t.penup()
        t.goto(110,-10)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[5] == "O":
        t.penup()
        t.goto(110,-10)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)
        
    if board[6] == "X":
        t.penup()
        t.goto(-180, -130)
        t.pensize(10)
        t.write("X",font=font)
    elif board[6] == "O":
        t.penup()
        t.goto(-180, -130)
        t.pensize(10)
        t.write("O",font=font)

    if board[7] == "X":
        t.penup()
        t.goto(-50,-130)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[7] == "O":
        t.penup()
        t.goto(-50,-130)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)     

    if board[8] == "X":
        t.penup()
        t.goto(110,-130)
        t.pensize(10)
        t.pendown()
        t.write("X",font=font)
    elif board[8] == "O":
        t.penup()
        t.goto(110,-130)
        t.pensize(10)
        t.pendown()
        t.write("O",font=font)
    
    
