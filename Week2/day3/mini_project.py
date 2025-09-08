#Representing the Game Board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
 ]
game_goes_on = True
winner = None
#creating the board
def display_board():
    print("***********")
    for i in range(0, 9, 3):
        print('*  ' + board[i] + '|' + board[i+1] + '|' + board[i+2] + '  *')
    print("***********")
display_board()