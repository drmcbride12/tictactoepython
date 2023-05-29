import random

# ANSI escape codes for colored text
RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'

# Prints the current state of the board with colors
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            if cell == 'X':
                print(RED + cell + END, end=" | ")
            elif cell == 'O':
                print(BLUE + cell + END, end=" | ")
            else:
                print(cell, end=" | ")
        print("\n-------------")

# Places the player's move on the board
def player_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print('That space is already taken. Please choose another space.')

# AI makes a move in easy mode
def easy_ai_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return

# AI makes a move in medium mode
def medium_ai_move(board):
    # Check if AI can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_win(board, 'O'):
                    return
                board[row][col] = ' '

    # Check if player can win in the next move and block them
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_win(board, 'X'):
                    board[row][col] = 'O'
                    return
                board[row][col] = ' '

    # Choose a random move
    easy_ai_move(board)

# AI makes a move in hard mode
def hard_ai_move(board):
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                available_moves.append((row, col))

    # Check for winning move
    for move in available_moves:
        row, col = move
        board[row][col] = 'O'
        if check_win(board, 'O'):
            return
        else:
            board[row][col] = ' '

    # Check for blocking move
    for move in available_moves:
        row, col = move
        board[row][col] = 'X'
        if check_win(board, 'X'):
            board[row][col] = 'O'
            return
        else:
            board[row][col] = ' '

    # Choose a random move
    random_move = random.choice(available_moves)
    row, col = random_move
    board[row][col] = 'O'

# AI makes a move in expert mode (minimax algorithm)
def expert_ai_move(board):
    best_score = float('-inf')
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
    scores = {'X': -1, 'O': 1, 'tie': 0}

    if check_win(board, 'X'):
        return scores['X']
    if check_win(board, 'O'):
        return scores['O']
    if check_tie(board):
        return scores['tie']

    if is_maximizing:
        best_score = float('-inf')
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

# Checks if the player has won
def check_win(board, player):
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

# Checks if the game has ended in a tie
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main function to play the game
def play_game():
    difficulty_levels = ['Easy', 'Medium', 'Hard', 'Expert', 'Impossible']
    player = 'X'

    print('Welcome to Tic Tac Toe!')
    print('You will play against the AI in increasing difficulty levels.')
    print('Your moves will be displayed in', RED + 'red', END, 'and the AI moves will be displayed in', BLUE + 'blue', END)
    input('Press Enter to start the game...')

    for current_level in range(len(difficulty_levels)):
        print('\n' + '=' * 20)
        print('Current Level:', difficulty_levels[current_level])
        print('=' * 20 + '\n')

        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # Initialize the board

        while True:
            print_board(board)

            if player == 'X':
                while True:
                    try:
                        row = int(input("Enter the row (1-3): ")) - 1
                        col = int(input("Enter the column (1-3): ")) - 1
                        if row in range(3) and col in range(3):
                            break
                        else:
                            print('Invalid input. Please enter numbers between 1 and 3.')
                    except ValueError:
                        print('Invalid input. Please enter numbers between 1 and 3.')

                player_move(board, row, col, player)

                if check_win(board, player):
                    print_board(board)
                    print('Congratulations! You won!')
                    break

                if check_tie(board):
                    print_board(board)
                    print('The game ended in a tie.')
                    break

                player = 'O'

            else:
                if difficulty_levels[current_level] == 'Easy':
                    easy_ai_move(board)
                elif difficulty_levels[current_level] == 'Medium':
                    medium_ai_move(board)
                elif difficulty_levels[current_level] == 'Hard':
                    hard_ai_move(board)
                else:
                    expert_ai_move(board)

                if check_win(board, 'O'):
                    print_board(board)
                    print('You lost! The AI won.')
                    break

                if check_tie(board):
                    print_board(board)
                    print('The game ended in a tie.')
                    break

                player = 'X'

        print('\n' + '=' * 20)
        print('Level completed:', difficulty_levels[current_level])
        print('=' * 20 + '\n')

        if current_level < len(difficulty_levels) - 1:
            input('Press Enter to proceed to the next level...')

    print('Congratulations! You have completed all levels.')

# Start the game
play_game()
