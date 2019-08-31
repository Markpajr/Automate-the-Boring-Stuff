import pprint
# Datastructures contain lists of dictionarires or lists
theBoard = {'top-L': 'X', 'top-M': 'X', 'top-R': 'X', 'mid-L': 'O', 'mid-M': 'X', 'mid-R': 'O', 'low-L': 'X', 'low-M': 'O', 'low-R': 'O'}


pprint.pprint(theBoard)


def printBoard(board):
    print(theBoard['top-L'] + '|'+theBoard['top-M']+'|'+theBoard['top-R'])
    print('-----')
    print(theBoard['mid-L'] + '|'+theBoard['mid-M']+'|'+theBoard['mid-R'])
    print('-----')
    print(theBoard['low-L'] + '|'+theBoard['low-M']+'|'+theBoard['low-R'])


printBoard(theBoard)
