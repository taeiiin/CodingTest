sudoku = []
blank = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))
def in_row(x, n):
    for i in range(9):
        if n == sudoku[x][i]:
            return False
    return True
def in_col(y, n):
    for i in range(9):
        if n == sudoku[i][y]:
            return False
    return True
def in_box(x, y, n):
    a = x//3 * 3
    b = y//3 * 3
    for i in range(3):
        for j in range(3):
            if n == sudoku[i+a][j+b]:
                return False
    return True
def dfs(n):
    if n == len(blank):
        for i in sudoku:
            print(*i)
        exit(0)
    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]
        if in_row(x, i) and in_col(y, i) and in_box(x, y, i):
            sudoku[x][y] = i
            dfs(n+1)
            sudoku[x][y] = 0
dfs(0)