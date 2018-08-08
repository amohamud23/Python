
board =[['','',''],['','',''],['','','']]


def drawBoard(board):
    print("-----------------")
    for i in board:
    
        for j in i:
            print(" ",j,end=' |')
    
        print()
        print("-----------------")
    return

#def switchPlayer(player)
    


def makeMove(board):
   row = int(input("Enter Row number (0,1,2): "))
   col = int(input("Enter Column number (0,1,2): "))
   board[row][col] = 'X'
   drawBoard(board)

def isWon(board):
    if board[0][0] == board[0][1] == board[0][2] :
        return True
    if board[1][0] == board[1][1] == board[1][2] :
        return True
    if board[2][0] == board[2][1] == board[2][2] :
        return True
    if board[0][0] == board[1][0] == board[2][0] :
        return True
    if board[0][1] == board[1][1] == board[2][1] :
        return True
    if board[0][2] == board[1][2] == board[2][2] :
        return True
    if board[0][0] == board[0][1] == board[0][2] :
        return True
    

while not isWon(board):
    drawBoard(board)
    makeMove(board)