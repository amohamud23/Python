
board =[['','',''],['','',''],['','','']]


def drawBoard(board):
    print("--------------")
    for i in board:
    
        for j in i:
            print(" ",j,end=' |')
    
        print()
        print("--------------")
    return

#def switchPlayer(player)
    


def makeMove(board, player):
    
   print("Player ", player, "'s Turn")
   row = int(input("Enter Row number (0,1,2): "))
   col = int(input("Enter Column number (0,1,2): "))
   board[row][col] = player
   
   

def isWon(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player :
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player :
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player :
        return True
    if board[0][0] == player and board[1][0] == player and board[2][0] == player :
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player :
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player :
        return True
    if board[0][0] == player and board[0][1] == player and board[0][2] == player :
        return True
    else:
        return False
    

while True:
    drawBoard(board)
    makeMove(board, 'X')
    if isWon(board, 'X'):
        print("Player X Won!")
        break

    drawBoard(board)
    makeMove(board, 'O')
    if isWon(board,'O'):
        print("Player O Won!")
        break
    