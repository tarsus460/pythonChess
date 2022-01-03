import pprint, time
chessBoard1 = {
    'a1':'wrook1','b1':'wknight1','c1':'wbishop1','d1':'wking1','e1':'wqueen1','f1':'wbishop2','g1':'wknight2','h1':'wrook2',
    'a2':'wpawn1','b2':'wpawn2','c2':'wpawn3','d2':'wpawn4','e2':'wpawn5','f2':'wpawn6','g2':'wpawn7','h2':'wpawn8',
    'a3':' ','b3':' ','c3':' ','d3':' ','e3':' ','f3':' ','g3':' ','h3':' ',
    'a4':' ','b4':' ','c4':' ','d4':' ','e4':' ','f4':' ','g4':' ','h4':' ',
    'a5':' ','b5':' ','c5':' ','d5':' ','e5':' ','f5':' ','g5':' ','h5':' ',
    'a6':' ','b6':' ','c6':' ','d6':' ','e6':' ','f6':' ','g6':' ','h6':' ',
    'a7':'bpawn1','b7':'bpawn2','c7':'bpawn3','d7':'bpawn4','e7':'bpawn5','f7':'bpawn6','g7':'bpawn7','h7':'bpawn8',
    'a8':'brook1','b8':'bknight1','c8':'bbishop1','d8':'bking1','e8':'bqueen1','f8':'bbishop2','g8':'bknight2','h8':'brook2',
                }
 
def moveCheck(pieceToMove,destination):
    for originSpace,originPiece in chessBoard1.items():
        if originPiece == pieceToMove:
            if originPiece[1:-1] == 'pawn':
                if destination[0] != originSpace[0] and destination[1] != str(int(originSpace[1]) +1): #the pawn must stay in the same column(destination[0]) and can only move forward 1 space
                    print('You can\'t move it there')
                    return False
            print('Moving '+ originPiece + ' at '+ originSpace+ ' to ' + destination)

#def captureCheck(turn,piece,destination):

#game begins here. White moves first 
turn = 'w'
 
while turn == 'w':
    pieceToMove = turn + input('Which piece would you like to move?')
    destination = input('Where would you like to move it?')
    if chessBoard1[destination] == ' ':
        moveCheck(pieceToMove,destination)
        if moveCheck(pieceToMove,destination) == False:
            continue
    #elif chessBoard1[destination] != ' ':
    #    captureCheck(turn,piece,destination)
#    chessBoard1[destination] = pieceToMove
    turn = 'b'