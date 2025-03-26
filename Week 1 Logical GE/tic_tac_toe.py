import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def get_user_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter 0, 1, or 2.")

def get_computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!\n")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            print("Computer's turn (O):")
            row, col = get_computer_move(board)
            board[row][col] = "O"
        else:
            print("Your turn (X):")
            row, col = get_user_move(board)
            board[row][col] = "X"
        
        print_board(board)
        
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            return
        elif check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            return
    
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
