# Tic Tac Toe Game Board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_board():
    for row in board:
        print(row)


def player_move(row, col, player):
    if board[row][col] == '-':
        board[row][col] = player
    else:
        print('That space is already taken. Please choose another space.')


# Test the functions
print_board()
player_move(0, 0, 'X')
print_board()
player_move(1, 1, 'O')
print_board()
