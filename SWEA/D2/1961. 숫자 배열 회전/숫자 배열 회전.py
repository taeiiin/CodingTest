T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
    temp90 = [[0]*n for _ in range(n)]
    temp180 = [[0]*n for _ in range(n)]
    temp270 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp90[j][n-i-1] = li[i][j]
            temp180[n-i-1][n-j-1] = li[i][j]
            temp270[n-j-1][i] = li[i][j]
    print("#%d" %test_case)
    for i in range(n):
        print(''.join(map(str, temp90[i])), ''.join(map(str, temp180[i])), ''.join(map(str, temp270[i])))