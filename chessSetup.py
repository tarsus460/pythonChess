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

piecesNeeded ={
'pawn': 8,
'rook': 2,
'knight': 2,
'bishop': 2,
'king': 1,
'queen': 1
}

whitePieces = {
    'pawn':0,
    'rook':0,
    'knight':0,
    'bishop':0,
    'king':0,
    'queen':0
}

blackPieces = {
    'pawn':0,
    'rook':0,
    'knight':0,
    'bishop':0,
    'king':0,
    'queen':0
}

#checks to makes sure each side has the correct number of pieces (16 per side)
whitePiecesCount = 0
blackPiecesCount = 0

for k,v in chessBoard1.items():
    if v.startswith('w'):
        whitePiecesCount += 1
    if v.startswith('b'):
        blackPiecesCount += 1
if blackPiecesCount == 16 and whitePiecesCount == 16:
    print(f'OK: number of pieces is {whitePiecesCount + blackPiecesCount}')
else:
    if whitePiecesCount != 16:
        print('ERROR: White has ' + str(whitePiecesCount) + ' pieces.')
    if blackPiecesCount != 16:
        print('ERROR: Black has ' + str(blackPiecesCount) + ' pieces.')
        
for k,v in chessBoard1.items():
    if v.startswith('w'):
        whitePieces[str(v)[1:]] += 1
    if v.startswith('b'):
        blackPieces[str(v)[1:]] += 1
        
 #game begins here. White moves first
 
turn = 'white'
 
while turn == 'white':
    pieceToMove = input('Which piece would you like to move?')
    space = input('Where would you like to move it?')
    chessBoard1[space] = pieceToMove
