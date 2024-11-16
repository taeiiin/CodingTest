T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    ing = [[0, 0]]
    for _ in range(n):
        ing.append(list(map(int, input().split())))
    dp = [[0]*(l+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, l+1):
            t = ing[i][0]
            k = ing[i][1]
            if j < k:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max((dp[i-1][j-k]+t), dp[i-1][j])
    print("#%d %d" %(test_case, dp[n][l]))