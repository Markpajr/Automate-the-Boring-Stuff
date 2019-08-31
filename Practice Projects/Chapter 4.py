
spam = ['cats', 'bats', 'rats', 'gats', 'lats']


def listconcat(origlist, separater: str):
    concatList = ''

    for i in origlist:
        if i == origlist[0]:
            concatList = concatList + str(origlist[origlist.index(i)])
        elif i != origlist[-1]:
            concatList = concatList + separater + str(origlist[origlist.index(i)])
        else:
            concatList = concatList + separater + 'and ' + str(origlist[origlist.index(i)])

    print(concatList)


listconcat(spam, ', ')


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rows = len(grid)
cols = len(grid[0])

for x in range(cols):
    for y in range(rows):
        print(grid[y][x], end='')
    print()
