T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    snail = [[0]*n for i in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    cnt = 1

    for _ in range(n*n):
        snail[x][y] = cnt
        nx, ny = x + dr[d], y + dc[d]
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d+1)%4
            x, y = x + dr[d], y + dc[d]
        cnt += 1

    print("#%d"%test_case)
    for i in snail:
        print(' '.join(map(str, i)))