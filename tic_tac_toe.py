import random

# ANSI escape codes for colored text
RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Prints the current state of the board with colors
def print_board():
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            if cell == 'X':
                print(RED + cell + END, end=" | ")
            elif cell == 'O':
                print(BLUE + cell + END, end=" | ")
            else:
                print(cell, end=" | ")
        print("\n---------")

# Places the player's move on the board
def player_move(row, col, player):
    if board[row-1][col-1] == ' ':
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
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return

# AI makes an improved move in hard mode
def hard_ai_move():
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                available_moves.append((row, col))

    # Check for winning move
    for move in available_moves:
        row, col = move
        board[row][col] = 'O'
        if check_win('O'):
            return
        else:
            board[row][col] = ' '

    # Check for blocking move
    for move in available_moves:
        row, col = move
        board[row][col] = 'X'
        if check_win('X'):
            board[row][col] = 'O'
            return
        else:
            board[row][col] = ' '

    # Choose a random move
    random_move = random.choice(available_moves)
    row, col = random_move
    board[row][col] = 'O'

# AI makes a move in impossible mode
def impossible_ai_move():
    best_score = -float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    row, col = best_move
    board[row][col] = 'O'

def minimax(board, depth, is_maximizing):
    if check_win('O'):
        return 1
    elif check_win('X'):
        return -1
    elif check_tie():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

# Checks if the game has ended in a tie
def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True

# Resets the board
def reset_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '

# Play a single game against the specified AI difficulty
def play_game(ai_difficulty):
    reset_board()
    print(f'Playing against {ai_difficulty} AI.')
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
        if ai_difficulty == 'Easy':
            easy_ai_move()
        elif ai_difficulty == 'Hard':
            hard_ai_move()
        elif ai_difficulty == 'Impossible':
            impossible_ai_move()
        print_board()
        if check_win('O'):
            print('Sorry, you lost. Better luck next time!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break

# Main function to start the game
def main():
    print('Welcome to Tic Tac Toe!')
    print('You need to beat the Easy, Hard, and Impossible AI in order to win.')

    while True:
        print('\n----- Easy Mode -----')
        play_game('Easy')
        print('You beat Easy AI!')

        print('\n----- Hard Mode -----')
        play_game('Hard')
        print('You beat Hard AI!')

        print('\n----- Impossible Mode -----')
        play_game('Impossible')
        print('You beat Impossible AI!')

        print('\nCongratulations! You beat all the AI difficulties!')
        play_again = input('Do you want to play again? (Y/N): ')
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()
