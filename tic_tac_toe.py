import random

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Prints the current state of the board
def print_board():
    for row in board:
        print(row)

# Places the player's move on the board
def player_move(row, col, player):
    if board[row-1][col-1] == '-':
        board[row-1][col-1] = player
    else:
        print('That space is already taken. Please choose another space.')

# Checks if the player has won
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

# AI makes a move in easy mode
def easy_ai_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '-':
            board[row][col] = 'O'
            return

# AI makes an improved move in hard mode
def hard_ai_move():
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                available_moves.append((row, col))

    # Check for winning move
    for move in available_moves:
        row, col = move
        board[row][col] = 'O'
        if check_win('O'):
            return
        else:
            board[row][col] = '-'

    # Check for blocking move
    for move in available_moves:
        row, col = move
        board[row][col] = 'X'
        if check_win('X'):
            board[row][col] = 'O'
            return
        else:
            board[row][col] = '-'

    # Choose a random move
    random_move = random.choice(available_moves)
    row, col = random_move
    board[row][col] = 'O'


# Checks if the game has ended in a tie
def check_tie():
    for row in board:
        if '-' in row:
            return False
    return True

# Runs the game in easy mode
def play_easy_mode():
    print('Playing in easy mode.')
    print('Welcome to Tic Tac Toe!')
    print_board()
    while True:
        # Player's move
        try:
            row = int(input('Enter row (1-3): '))
            col = int(input('Enter column (1-3): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 3.')
            continue
        if row < 1 or row > 3 or col < 1 or col > 3:
            print('Invalid input. Please enter a number between 1 and 3.')
            continue
        player_move(row, col, 'X')
        print_board()
        if check_win('X'):
            print('Congratulations! You won!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break
        # AI's move
        print('AI is making a move...')
        easy_ai_move()
        print_board()
        if check_win('O'):
            print('Sorry, you lost. Better luck next time!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break

# Runs the game in hard mode
def play_hard_mode():
    print('Playing in hard mode.')
    print('Welcome to Tic Tac Toe!')
    print_board()
    while True:
        # Player's move
        try:
            row = int(input('Enter row (1-3): '))
            col = int(input('Enter column (1-3): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 3.')
            continue
        if row < 1 or row > 3 or col < 1 or col > 3:
            print('Invalid input. Please enter a number between 1 and 3.')
            continue
        player_move(row, col, 'X')
        print_board()
        if check_win('X'):
            print('Congratulations! You won!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break
        # AI's move
        print('AI is making a move...')
        hard_ai_move()
        print_board()
        if check_win('O'):
            print('Sorry, you lost. Better luck next time!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break

# Main function to choose game mode and start the game
def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        try:
            mode = int(input('Choose a game mode:\n1. Easy\n2. Hard\nEnter the mode number (1-2): '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue
        if mode == 1:
            play_easy_mode()
            break
        elif mode == 2:
            play_hard_mode()
            break
        else:
            print('Invalid input. Please enter 1 for Easy mode or 2 for Hard mode.')

if __name__ == '__main__':
    main()
