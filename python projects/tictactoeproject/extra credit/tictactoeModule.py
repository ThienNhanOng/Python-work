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

"""
def win(board, symbol):
    # Win Conditions for Row 1-3
    for index in range(0, 9, 3):
        if board[index] == board[index + 1] == board[index + 2] == symbol:
        # Win Conditions for Column 1-3
            return True
        if board[0] == symbol and board[3] == symbol and board[6] == symbol:
            return True
        if board[1] == symbol and board[4] == symbol and board[7] == symbol:
            return True
        if board[2] == symbol and board[5] == symbol and board[8] == symbol:
            return True
        # Win Conditions for Diagonals
        if board[0] == symbol and board[4] == symbol and board[8] == symbol:
            return True
        if board[2] == symbol and board[4] == symbol and board[6] == symbol:
            return True


def displayBoard(board):
    print(f"{board[0]}  {board[1]}  {board[2]}")   #prints out the board
    print(f"{board[3]}  {board[4]}  {board[5]}")
    print(f"{board[6]}  {board[7]}  {board[8]}")

def getMove(board, player, locations):  # allow player1 or player 2 to move
    move = int(input(f"{player}, enter your move: "))
    while str(move) not in locations:
        move = int(input("Invalid number! Try again!\n"))  # if input is not in locations ask user to reinput
    while board[move - 1] == 'X' or board[move - 1] == 'O':
        move = int(input("This spot is taken! Try again!\n"))  # if spot already has a "X" or "O", ask user to reinput
    else:
        return move - 1

def tieGame(board): # checks for empty spot on list
    for index in board:
        if index == ("-"):
            return False
    return True
