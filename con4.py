import numpy as np
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = 0
PLAYER = 1
COMPUTER = 2

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r
    return -1

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if all([board[r][c+i] == piece for i in range(4)]):
                return True

    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if all([board[r+i][c] == piece for i in range(4)]):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if all([board[r+i][c+i] == piece for i in range(4)]):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if all([board[r-i][c+i] == piece for i in range(4)]):
                return True

def get_valid_moves(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def computer_move(board):
    valid_moves = get_valid_moves(board)
    for col in valid_moves:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, COMPUTER)
        if winning_move(temp_board, COMPUTER):
            return col
    return random.choice(valid_moves) if valid_moves else None

def main():
    board = create_board()
    game_over = False
    print_board(board)

    while not game_over:
        # User's move
        col = int(input("Your Turn! (0-6): "))
        if col not in get_valid_moves(board):
            print("Invalid move. Try again.")
            continue

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, PLAYER)

        if winning_move(board, PLAYER):
            print_board(board)
            print("Congratulations! You win!")
            break

        if len(get_valid_moves(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        # Computer's move
        col = computer_move(board)
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, COMPUTER)

        if winning_move(board, COMPUTER):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        print_board(board)

if __name__ == "__main__":
    main()
