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


def check_win(player):
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def ai_move():
    import random
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while board[row][col] != '-':
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = 'O'


def check_tie():
    for row in board:
        if '-' in row:
            return False
    return True


# Test the functions
print_board()
player_move(0, 0, 'X')
ai_move()
print_board()
print(check_win('X'))
print(check_win('O'))
print(check_tie())
