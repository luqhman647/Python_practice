import fun
import os
# clearing the terminal
os.system('cls')
# displaying the rules and taking the player names
fun.rules()
player1 = input('\nplayer1, Enter your name: ' )
player2 = input('player2, Enter your name: ' )
# declaring the variables required
player = [player1, player2]
var = {11:' ',12:' ',13:' ',21:' ',22:' ',23:' ',31:' ',32:' ',33:' ',}
turn, false_turn = 1, 0
playing, complete = True, False
# game loop
while playing :
    #clearing the terminal
    os.system('cls') 
    # drawing the current game board 
    fun.board(var)   
    # displaying if invalid selection happens
    if false_turn == turn:
        print('Invalid selection, select again: ')
    false_turn = turn
    # getting valid input from the user
    choice = input(f"\nEnter the row and column of your move(e.g. 12)\n{player[(turn % 2)-1]}'s turn: ")
    # if the selection is valid storing it 
    if choice.isdigit() and int(choice) in var.keys() and var[int(choice)] == ' ':
        var[int(choice)] = fun.whose_turn(turn)
        turn += 1
    # checking for win condition after users selection
    if fun.win_condition(var): 
        playing, complete = False, True
    if turn > len(var): 
        playing = False
# if the game has ended displaying the final board
os.system('cls')    
fun.board(var)
# displaying the end result
if complete:
    if fun.whose_turn(turn) == 'O':
        print(f'\nCongratulations {player[0]}! You Won')
    else:
        print(f'\nCongratulations {player[1]}! You Won')
else: 
    print('\nIts a draw')    


   
           

        

  
                    