def dfs(row):
    global result
    if row == n:
        result += 1
        return
    for i in range(n):
        valid = True
        for j in range(row):
            if col[j] == i or abs(row - j) == abs(i - col[j]):
                valid = False
                break
        if valid:
            col[row] = i
            dfs(row + 1)
            col[row] = -1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    col = [-1]*n
    result = 0
    dfs(0)
    print("#%d %d" %(test_case, result))