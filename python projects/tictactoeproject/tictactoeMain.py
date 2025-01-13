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


import tictactoeModule

def main():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("This program will allow two players to play a game of tic-tac-toe.")
    print("Player 1 has 'X', and player 2 has 'O'")
    player1 = input("Enter the name of player1: ")
    player2 = input("Enter the name of player2: ")
    print("Enter your mark using the board positions shown below")
    print(" 1  2  3 \n 4  5  6 \n 7  8  9")

    player1_symbol = "X"
    player2_symbol = "O"
    print(player1, " you start. You are playing as 'X'.")

    tictactoeModule.displayBoard(board)

    game_over = False
    while not game_over:
        # takes a move and put X in the spot on the board
        board[tictactoeModule.getMove(board, player1, locations)] = player1_symbol  #takes player1's move and puts X in its position
        tictactoeModule.displayBoard(board)     #displays the current board
        game_over = tictactoeModule.win(board, player1_symbol)
        if game_over:   #this ends the game if player1 wins
            print(player1, ", you win!")
            break

        tie_game = tictactoeModule.tieGame(board)
        if tie_game:
            print(player1, "and", player2, "ended in a tie!")
            break


        # takes a move and put O in the spot on the board
        board[tictactoeModule.getMove(board, player2, locations)] = player2_symbol
        tictactoeModule.displayBoard(board)
        game_over = tictactoeModule.win(board, player2_symbol)
        if game_over:   #this ends the game if player2 wins
            print(player2, ", you win!")
            break


main()
