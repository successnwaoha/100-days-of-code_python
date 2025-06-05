import random
from os import system

BOARD = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    for i in range(len(board)):
        print(" | ".join(board[i]))
        if i < len(board) - 1:
            print("-" * 9)

def is_valid_move(board, row, column):
    if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
        return False
    
    if board[row][column] != ' ':
        return False   
    return True

def check_winner(board):
    #Check rows (Horizontally)
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0] #Return the winner ('X' or 'O')
    
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != ' ':
            return board[0][column] #Return the winner ('X' or 'O')
        
    #Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0] #Return the winner ('X' or 'O')
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2] #Return the winner ('X' or 'O')
    
def is_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def play(row, column, player):
    BOARD[row][column] = player
    
def get_valid_move(board):
    while True:
        try:
            user_row = int(input("Please enter the ROW (0-2): "))
            user_column = int(input("Please enter the COLUMN (0-2): "))
            if user_row < 0 or user_row > 2 or user_column < 0 or user_column > 2:
                print("Invalid input! row and column must be between 0 and 2.")
                continue
            return user_row, user_column
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
continue_game = True
current_player = 'X'

while continue_game:
    invalid_move = True
    while invalid_move:
        print(f"{current_player}'s turn")
        user_row, user_column = get_valid_move(BOARD)
        
        if is_valid_move(BOARD, user_row, user_column):
            play(user_row, user_column, current_player)
            print_board(BOARD)
            
            if check_winner(BOARD):
                print(f"{current_player} wins!!")
                continue_game = False
                invalid_move = False
    
            elif is_tie(BOARD):
                print("It's a tie!!")
                continue_game = False
                invalid_move = False
    
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
            invalid_move = False
        else:
            print("Invalid move! Try again")