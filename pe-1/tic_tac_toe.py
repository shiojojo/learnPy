from random import randrange

board = [
    [1,2,3],
    [4,"X",6],
    [7,8,9]
    ]
sign = ""
    
def display_board(board):
    for i in range(0,len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + str(board[i][0]) + "   |   " + str(board[i][1]) + "   |   " + str(board[i][2]) + "   |")
        print("|       |       |       |")
    else:
        print("+-------+-------+-------+")
    

def enter_move(board):
    while True:
        try:
            your_move = int(input("Enter your move: "))
            row = (your_move - 1) // 3
            column = (your_move - 1) % 3
            if board[row][column] not in ["X" ,"O"]:
                board[row][column] = "O"
                break
        except Exception as e:
            print(e.__class__.__name__)
            exit()

def make_list_of_free_fields(board):
    free_fields = []
    for j in range(3):
        for k in range(3):
             if board[j][k] not in ['O','X']: 
                free_fields.append((j,k))
    return free_fields
                    
def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            sign = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i]:
            sign = board[0][i]
            break
    if board[0][0] == board[1][1] == board[2][2] \
        or board[0][2] == board[1][1] == board[2][0]:
        sign = "X"
    if sign == "X":
        print("Your Lose")
        return "X"
    elif sign == "O":
        print("Your Win")
        return "O"

def draw_move(board):
    while True:
        computer_move = randrange(1,10)
        row = (computer_move - 1) // 3
        column = (computer_move - 1) % 3
        if board[row][column] not in ["X" ,"O"]:
            board[row][column] = "X"
            break

free_fields_list = make_list_of_free_fields(board)
while len(free_fields_list):
    display_board(board)
    enter_move(board)
    sign = victory_for(board, sign)
    if sign == "O":
        display_board(board)
        break
    draw_move(board)
    sign = victory_for(board, sign)
    if sign == "X":
        display_board(board)
        break
    free_fields_list = make_list_of_free_fields(board)
else:
    print(" a tie")
    display_board(board)



