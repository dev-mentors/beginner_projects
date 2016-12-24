#George Apostolopoulos
from Board import Board
# from Cell import Cell

# need to create tic-tac-toe board of 3 x 3 square (9 total squares)
# need to check if you have won (8 lines total)
# ask the input of 2 players
# create commands to place X's and O's
# create code to check if x or o is already placed

board = Board()

# print board

# board.player_mark(2,1,"x")
# board.player_mark(2,1,"x")
# board.player_mark(2,0,"x")

print board


player = "x".lower()


while board.check_won("x") is False and board.check_won("o") is False:

    print "Current player is " + player

    while True:
        row_position = int(raw_input("What row would you like to place your mark?: "))
        col_position = int(raw_input("What column would you like to place your mark?: "))

        if row_position and col_position not in xrange(0, 3):
            print "Error! Yoy may only enter digits 0-2! "
            if player == "x":
                player = "o"
            elif player == "o":
                player = "x"

            break

        if board.is_empty(row_position, col_position) is True:
            board.player_mark(row_position, col_position, player)
            break
        else:
            print "Invalid position, please place again. "

    print board

    if player == "x":
        player = "o"
    elif player == "o":
        player = "x"


if board.check_won("x") is True:
    print "player X has won"
elif board.check_won("o") is True:
    print "player O has won"
else:
    print "Unexpected error occurred"
