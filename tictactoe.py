
board =[['','',''],['','',''],['','','']]


def drawBoard(board):
    print("-----------------")
    for i in board:
    
        for j in i:
            print(" ",j,end=' |')
    
        print()
        print("-----------------")
    return



def makeMove(board):
   row = int(input("Enter Row number (0,1,2): "))
   col = int(input("Enter Column number (0,1,2): "))
   board[row][col] = 'X'
   drawBoard(board)

drawBoard(board)
makeMove(board)