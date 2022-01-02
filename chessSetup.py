import pprint, time
chessBoard1 = {
    'a1':'wrook','b1':'wknight','c1':'wbishop','d1':'wking','e1':'wqueen',
    'f1':'wbishop','g1':'wknight','h1':'wrook','a2':'wpawn','b2':'wpawn',
    'c2':'wpawn','d2':'wpawn','e2':'wpawn','f2':'wpawn','g2':'wpawn','h2':'wpawn',
    'a8':'brook','b8':'bknight','c8':'bbishop','d8':'bking','e8':'bqueen','f8':'bbishop','g8':'bknight',
    'h8':'brook','a7':'bpawn','b7':'bpawn','c7':'bpawn','d7':'bpawn','e7':'bpawn','f7':'bpawn','g7':'bpawn',
    'h7':'bpawn'
                }
#TODO: setup logfile system


 
def moveCheck(turn,piece,origin,destination):
    if turn == 'w':
        #add to key index 1
        if piece.startswith(turn+'pawn'):
            piece
    elif turn == 'b':
        #subtract from key index 1

#game begins here. White moves first 
turn = 'w'
 
while turn == 'w':
    pieceToMove = input('Which piece would you like to move?')
    space = input('Where would you like to move it?')
    chessBoard1[space] = pieceToMove
    turn = 'b'