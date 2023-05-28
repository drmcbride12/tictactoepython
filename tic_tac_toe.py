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

# AI makes a random move
def ai_move():
    import random
    row = random.randint(1, 3)
    col = random.randint(1, 3)
    while board[row-1][col-1] != '-':
        row = random.randint(1, 3)
        col = random.randint(1, 3)
    board[row-1][col-1] = 'O'

# Checks if the game has ended in a tie
def check_tie():
    for row in board:
        if '-' in row:
            return False
    return True

# Runs the game
def main():
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
        ai_move()
        print_board()
        if check_win('O'):
            print('Sorry, you lost. Better luck next time!')
            break
        if check_tie():
            print('The game ended in a tie.')
            break

if __name__ == '__main__':
    main()
