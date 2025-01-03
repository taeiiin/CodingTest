T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    bag = [[0, 0]]
    dp = [[0]*(k+1) for _ in range(n+1)]
    for _ in range(n):
        bag.append(list(map(int, input().split())))
    for i in range(1, n+1):
        for j in range(1, k+1):
            w, v = bag[i][0], bag[i][1]
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    print("#%d %d" %(test_case, dp[n][k]))