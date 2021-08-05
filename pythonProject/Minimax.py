import main
player = ['O', 'X']
def minimax(board, depth, isMax):
    winner = main.get_winner(board)

    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10

    if any('-' in sub for sub in board) == False:
        return 0

    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '-'):
                    board[i][j] = player[0]
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '-'
        return best
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '-'):
                    board[i][j] = player[1]
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '-'
        return best


def findBestMove(board):

    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if (board[i][j] == '-'):
                board[i][j] = player[0]

                moveVal = minimax(board, 0, False)

                board[i][j] = '-'

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove