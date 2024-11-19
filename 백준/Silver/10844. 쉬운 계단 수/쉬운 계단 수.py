n = int(input())
MOD = 1000000000
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for l in range(2, n + 1):
    for d in range(10):
        if d == 0:
            dp[l][d] += dp[l - 1][1]
        elif d == 9:
            dp[l][d] += dp[l - 1][8]
        else:
            dp[l][d] += dp[l - 1][d - 1] + dp[l - 1][d + 1]
        dp[l][d] %= MOD

result = sum(dp[n]) % MOD
print(result)