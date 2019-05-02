grid = []
for i in range(3):
    grid.append(input().split())

for i in range(3):
    for j in range(3):
        if(grid[i][j] != 'X'):
            grid[i][j] = int(grid[i][j])

for idx, row in enumerate(grid):
    if(row.count('X') == 1):
        if(row[1] == 'X'):
            grid[idx][1] = int((max(row[0], row[2]) - min(row[0], row[2]))/2 + min(row[0], row[2]))
        elif(row[0] == 'X'):
            grid[idx][0] = int(row[1] - (row[2] - row[1]))
        elif(row[2] == 'X'):
            grid[idx][2] = int(row[1] - (row[0] - row[1]))

for i in range(3):
    curCol = []
    for j in range(3):
        curCol.append(grid[j][i])
    if(curCol.count('X') == 1):
        if(curCol[1] == 'X'):
            grid[1][i] = int((max(curCol[0], curCol[2]) - min(curCol[0], curCol[2]))/2 + min(curCol[0], curCol[2]))
        elif(curCol[0] == 'X'):
            grid[0][i] = int(curCol[1] - (curCol[2] - curCol[1]))
        elif(curCol[2] == 'X'):
            grid[2][i] = int(curCol[0] - (curCol[1] - curCol[0]))

for i in grid:
    for j in i:
        print(j, end='')
        print(' ', end='')
    print('')