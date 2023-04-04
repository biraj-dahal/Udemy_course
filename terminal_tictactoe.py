# Modules to download
from tkinter import *

game_board = [['-','-','-'],['-','-','-'],['-','-','-']]

# Function used later in the program
def print_board(game_board):
    print()
    for i in range(len(game_board)):
        print("  |", end = "  ")
        for j in range(len(game_board)):
            print(game_board[i][j], end =  "  |  ")
        print()
        print()
    print()

def check_valid_move(game_board, move):
    if game_board[int(move[0])-1][int(move[1])-1] == '-':
        return True
    return False

def check_row_over(game_board):
    if game_board[0][0] ==  game_board[0][1] ==  game_board[0][2] and game_board[0][0] != '-':
        return True
    elif game_board[1][0] ==  game_board[1][1] ==  game_board[1][2] and game_board[1][0] != '-':
        return True
    elif game_board[2][0] == game_board[2][1] ==  game_board[2][2] and game_board[2][0] != '-':
        return True
    else: 
        return False
    
def check_column_over(game_board):
    if game_board[0][0] == game_board[1][0] == game_board[2][0]  and game_board[0][0] != '-':
        return True
    elif game_board[0][1] == game_board[1][1] == game_board[2][1] and game_board[0][1] != '-':
        return True
    elif game_board[0][2] == game_board[1][2] == game_board[2][2] and game_board[0][2] != '-':
        return True
    else: 
        return False

def check_diagnal_over(game_board):
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != '-':
        return True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0]and game_board[0][2] != '-':
        return True
    else: 
        return False
    
def game_play(game_board, player_1, player_2, player_dict):
    turn = 1
    while turn != 10 and  not (check_column_over(game_board)) and  not(check_row_over(game_board)) and  not( check_diagnal_over(game_board)):
        player = player_1 if turn % 2 == 1 else player_2
        print(f"\n\nIt is {player}'s turn to play and place {player_dict[player]} on the game board\nPlease enter in rowcol format.\n")

        print_board(game_board)
        move = input()
        if move not in ["11", "12", "13", "21", "22", "23", "31", "32", "33"] or (not check_valid_move(game_board, move)):
            print("invalid Move. Please Try Again.")
            continue
        game_board[int(move[0])-1][int(move[1])-1] = player_dict[player]
        turn += 1
    if turn == 10:
        print(''' ******************** \n
        We have a draw \n
        ********************\n''')
        print_board(game_board)
    else:
        print(f''' ******************** \n
        We have a winner. Congratulations {player} for winning! \n
        ********************\n''')
        print_board(game_board)
# tkinter functions 
# def get_first_name():
#     global player_1
#     player_1 = e.get()
#     window_content.config(text= f'''\n\nWelcome to the Tic-Tac-Game Folks!\n\n\n\n\n\n\n\n\nEnter Second Person's name\n\n''')
#     button.config(command = get_second_name)
# def get_second_name():
#     global player_2
#     player_2 = e.get()
#     e.destroy()
#     button.destroy()
#     space_label.destroy()
#     player_dict = {player_1 : 'O', player_2 : 'X'}
#     game_play(game_board, player_1, player_2, player_dict)


# Tkinter GUI
# window = Tk()
# window.geometry("500x500+500+200")
# window.title("Tic-Tac-Toe")
# window.resizable(False,False)
# click = True
# turn = 1

# btn1 = StringVar()
# btn2 = StringVar()
# btn3 = StringVar()
# btn4 = StringVar()
# btn5 = StringVar()
# btn6 = StringVar()
# btn7 = StringVar()
# btn8 = StringVar()
# btn9 = StringVar()
# xPhoto = PhotoImage(file= "xphoto.png")
# ophoto = PhotoImage(file = "ophoto.png")

# window_content = Label(window, text= f'''\n\nWelcome to the Tic-Tac-Game Folks!\n\n\n\n\n\n\n\n\nEnter First Person's name\n\n''', font= ("Helvetica", 15,"italic"), fg="white")
# window_content.pack()
# e = Entry(window, width = 20, font=("Helvetica", 20,))
# button = Button(window, text="Submit", command=get_first_name)
# e.pack()
# button.pack()
# space_label = Label(window, text= f'''\n\n\n\n\n\n\n\n\n\n\n\n''', font= ("Helvetica", 15,"italic"), fg="white")
# space_label.pack()


# window.mainloop()

# Initializer     
player_1 = input("Enter Player 1 Name: ")
player_2 = input("Enter Player 2 Name: ")
player_dict = {player_1 : 'O', player_2 : 'X'}
game_play(game_board, player_1, player_2, player_dict)




