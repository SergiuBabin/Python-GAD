import Minimax

positions_groups = (
    [[(x, y) for y in range(3)] for x in range(3)] +  # horizontals
    [[(x, y) for x in range(3)] for y in range(3)] +  # verticals
    [[(d, d) for d in range(3)]] +  # diagonal
    [[(2-d, d) for d in range(3)]]  # diagonal
)

def get_winner(board):
    for positions in positions_groups:
        values = [board[x][y] for (x, y) in positions]
        if len(set(values)) == 1 and values[0] and values[0] != '-':
            return values[0]

def print_format(vals):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(vals[0][0], vals[0][1], vals[0][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(vals[1][0], vals[1][1], vals[1][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(vals[2][0], vals[2][1], vals[2][2]))
    print("\t     |     |")
    print("\n")




def turn(player, board):
    print("Player {} turn".format(player + 1))
    move_x = input("line = ")
    move_y = input("colomn = ")

    if player == 1:
        if board[int(move_x) - 1][int(move_y) - 1] != '-':
            return False
        board[int(move_x) - 1][int(move_y) - 1] = 'X'
    elif player == 0:
        if board[int(move_x) - 1][int(move_y) - 1] != '-':
            return False
        board[int(move_x) - 1][int(move_y) - 1] = 'O'
    else:
        print("Player engine turn")
        (x, y) = Minimax.findBestMove(board)
        board[x][y] = 'X'
    return True

def game_2_people(player, board):
    print_format(board)
    while True:
        check = turn(player, board)
        print_format(board)

        if check != True:
            print("Ilegal move\nTry again")
        else:
            player = 1 - player

        if get_winner(board) != None:
            break

        if any('-' in sub for sub in board) != True:
            break

    print("Winner {}".format(get_winner(board)))

def game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    print("Python game Tik_tak_toe start\n")
    player = input("Please select player: X (1) or O (0)\n")
    player = int(player)

    if player == 1:
        print("You play with X")
    elif player == 0:
        print("You play with O")
    else:
        print("You play with O and Engine play with X")
        player == 0


    print("This is game board with 3 lines and 3 colomns.")
    print("You need to introduce line and colomn on your move.")

    game_2_people(player, board)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

