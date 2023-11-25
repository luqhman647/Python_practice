# function to display the rules of  the game
def rules():
    print('''TIC TAC TOE\n
    Rules:
          The game will be played in the terminal, and the game board will be displayed as a 3x3 grid.
          Players take turns marking a square with their designated letter (X or O).
          The first player to have 3 of their marks in a row (horizontally, vertically, or diagonally) is the winner.
          If all of the squares are filled and no player has 3 marks in a row, the game is a draw.''')

# function to manage the board of the game 
def board(dict):
    print(f' {dict[11]} | {dict[12]} | {dict[13]}')
    print('---+---+---')
    print(f' {dict[21]} | {dict[22]} | {dict[23]}')
    print('---+---+---')
    print(f' {dict[31]} | {dict[32]} | {dict[33]}')

# function to navigate the players turn
def whose_turn(turn):
    if turn % 2 == 1:
        return 'X'
    else:
        return 'O'

# function to check the win condition of the game
def win_condition(dict):
    if     (dict[11] == dict[12] == dict[13] != ' ')\
        or (dict[21] == dict[22] == dict[23] != ' ')\
        or (dict[31] == dict[32] == dict[33] != ' '):
        return True
    
    elif   (dict[11] == dict[21] == dict[31] != ' ')\
        or (dict[12] == dict[22] == dict[32] != ' ')\
        or (dict[13] == dict[23] == dict[33] != ' '):
        return True
    
    elif    (dict[11] == dict[22] == dict[33] != ' ') \
         or (dict[13] == dict[22] == dict[31] != ' '):
        return True
    
    else: return False