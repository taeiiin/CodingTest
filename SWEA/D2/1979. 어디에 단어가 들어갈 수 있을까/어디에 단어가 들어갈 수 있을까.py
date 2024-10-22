T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    board_f = list(map(list, zip(*board)))
    cnt = 0
    for i in board+board_f:
        x = ''.join(map(str, i)).split('0')
        for j in x:
            if len(j) == k:
                cnt += 1
    print("#%d %d" %(test_case, cnt))