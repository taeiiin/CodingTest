from collections import deque
def bfs(i, j):
    q = deque()
    q.append((i, j))
    result[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if result[x][y] + maps[nx][ny] < result[nx][ny]:
                result[nx][ny] = result[x][y] + maps[nx][ny]
                q.append((nx, ny))

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    maps = []
    result = [[float('inf')] * n for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for _ in range(n):
        maps.append(list(map(int, input().strip())))
    bfs(0, 0)
    print("#%d %d" % (test_case, result[n-1][n-1]))