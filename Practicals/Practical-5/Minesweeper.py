import random

run = True
numCount = 0
mainList = [] 
mineList = [] 
print('''
Welcome to Minesweeper!

Instructions:
1. Enter the board size (e.g., 3 for a 3x3 board).
2. Enter row and column numbers to reveal a cell.
3. Avoid the mines and reveal all non-mine cells to win.

Board sizes:
- 3 for 3x3 = 9 cells
- 4 for 4x4 = 16 cells
''')
while True:
    try:
        boardSize = int(input("Enter board size (e.g., 3 for 3x3): "))
        if boardSize > 1:
            break
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
n = int((boardSize**2) * 0.25)
mineList = random.sample([(x, y) for x in range(boardSize) for y in range(boardSize)], n)
mainList = [['-' for _ in range(boardSize)] for _ in range(boardSize)]
def countNeighborMines(row, col, mineList):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        if (row + dr, col + dc) in mineList:
            count += 1
    return count
def currentBoardStatus(boardSize, mainList):
    print("\n  " + " ".join(map(str, range(boardSize)))) 
    for i in range(boardSize):
        print(i, " ".join(map(str, mainList[i]))) 
print("\nHere starts your Minesweeper Game.")
while run:
    currentBoardStatus(boardSize, mainList)
    while True:
        try:
            row = int(input("Enter row number: "))
            column = int(input("Enter column number: "))
            if 0 <= row < boardSize and 0 <= column < boardSize:
                break
            else:
                print("Invalid choice. Please select numbers within the board range.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    if (row, column) in mineList:
        print("\nYou hit a mine! Game Over!")
        run = False
        for a, b in mineList:
            mainList[a][b] = '*'
    else:
        if mainList[row][column] == '-':
            mainList[row][column] = countNeighborMines(row, column, mineList)
            numCount += 1
    if numCount == boardSize**2 - n:
        print("\nCongratulations! You won!")
        run = False
currentBoardStatus(boardSize, mainList)
