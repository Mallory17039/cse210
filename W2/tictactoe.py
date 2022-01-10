"""
TIcTacToe
Author: Mallory Lee
"""

# Board
board = {'7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' }

current_player = "X"
winner = None
game_Running = True
selection = []
count = 0

# printing the game board
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# input from players
def player_select(board):
    global count
    ##### HOW TO CHECK IS THAT NUMBER IS TAKEN
    print(f"{current_player}, It is your turn.")
    select = int(input("Enter a number 1-9: "))
    if select >= 1 and select <= 9 and (select not in selection):
        select = str(select)
        board[select] = current_player

        for i in board:
            selection.append(i)

        count += 1
    else:
        print("That number is already taken!")

# Check win or tie
def check_Horizontle(board):
    global winner
    if board['7'] == board['8'] == board['9'] and board['7'] != ' ':
        winner = board['7']
        return True
    elif board['4'] == board['5'] == board['6'] and board['4'] != ' ':
        winner = board['4']
        return True
    elif board['1'] == board['2'] == board['3'] and board['1'] != ' ':
        winner = board['1']
        return True

def check_Row(board):
    global winner 
    if board['7'] == board['4'] == board['1'] and board['7'] != ' ':
        winner = board['7']
        return True
    elif board['8'] == board['5'] == board['2'] and board['8'] != ' ':
        winner = board['8']
        return True
    elif board['9'] == board['6'] == board['3'] and board['9'] != ' ':
        winner = board['9']
        return True

def check_Diagnal(board):
    global winner 
    if board['7'] == board['5'] == board['3'] and board['7'] != ' ':
        winner = board['7']
        return True
    elif board['1'] == board['5'] == board['9'] and board['1'] != ' ':
        winner = board['1']
        return True

def check_tie(board):
    global count
    global game_Running
    if count == 9:
        printBoard(board)
        print("It's a tie!")
        game_Running = False

def check_win():
    global game_Running
    if check_Diagnal(board) or check_Horizontle(board) or check_Row(board):
        print(f"The winner is {winner}")
        game_Running = False


# Switch the Player
def switchPlayer():
    global current_player
    if current_player == "X":
        current_player == "O"
    else:
        current_player == "X"

def main():
    while game_Running:
        printBoard(board)
        player_select(board)
        check_win()
        check_tie(board)
        switchPlayer()

if __name__ == "__main__":
    main()