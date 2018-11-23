def print_board(board):
    print(board[7],"|",board[8],"|",board[9])
    print("---------")
    print(board[4],"|",board[5],"|",board[6])
    print("---------")
    print(board[1],"|",board[2],"|",board[3])
    print('')

def make_move(board,player,move):
    board[move] = player




myBoard=[' ']*10 

print_board(myBoard)

myBoard[1] = 'X'

print_board(myBoard)