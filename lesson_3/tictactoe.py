import random
import os

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'

board = {
    1: ' ',     # top    left
    2: ' ',            # center
    3: ' ',            # right
    4: ' ',     # middle left
    5: ' ',            # center
    6: ' ',            # right
    7: ' ',     # bottom left
    8: ' ',            # center
    9: ' ',            # right
} # 𝕏 𝕆
#remaining = ['X', 'X', 'X', 'O', 'O', 'O']

def display_board(board):
    os.system('clear')
    
    print(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('       𝕋𝕚𝕔𝕥𝕒𝕔𝕥𝕠𝕣𝕚𝕠!        ')
    print('╔═══════╦═══════╦═══════╗')
    print('║       ║       ║       ║')
    print(f'║   {board[1]}   ║   {board[2]}   ║   {board[3]}   ║')
    print('║       ║       ║       ║')
    print('╠═══════╬═══════╬═══════╣')
    print('║       ║       ║       ║')
    print(f'║   {board[4]}   ║   {board[5]}   ║   {board[6]}   ║')
    print('║       ║       ║       ║')
    print('╠═══════╬═══════╬═══════╣')
    print('║       ║       ║       ║')
    print(f'║   {board[7]}   ║   {board[8]}   ║   {board[9]}   ║')
    print('║       ║       ║       ║')
    print('╚═══════╩═══════╩═══════╝')
#   print('╠═══════╩═══════╩═══════╣')
#   print('║Remaining: X O X O X O ║')
#   print('╚═══════════════════════╝')
    print('        ꧁═════꧂        ')

def initialize_board():
    return {
        num: INITIAL_MARKER for num in range(1, 10)
    }

def prompt(message):
    print(f'> {message}')
    return input('> ').strip()

def display_message(message):
    print(f'> {message}')

def empty_squares(board):
    return [key 
            for key, value in board.items() 
            if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
#       square = prompt(f"Choose a square ({', '.join(map(str, empty_squares))}):")
        square = int(prompt(
            f'Choose a square: \n({", ".join([str(num) for num in empty_squares(board)])})'
        ))
        if square in empty_squares(board):
            break
        
        print('Sorry, that\'s not a valid choice.')
    
    board[square] = PLAYER_MARKER

def computer_chooses_square(board):
    if board_full(board):
        return
    
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER 
            and board[sq2] == PLAYER_MARKER 
            and board[sq3] == PLAYER_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER 
            and board[sq2] == COMPUTER_MARKER 
            and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    
    return None



def play_tic_tac_toe():
    while True:
        board = initialize_board()
        print('Welcome to Tictactorio! 𝕏𝕆')
        
        while True:
            display_board(board)
            
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            
            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
        
        display_board(board)
        
        if someone_won(board):
            display_message(f'{detect_winner(board)} wins!')
        else:
            display_message('It\'s a tie!')
        
        answer = str(prompt('Play again? (y or n)')).lower()
        
        if answer[0] != 'y':
            break
    
    print('Thanks for playing Tictactorio!')

play_tic_tac_toe()