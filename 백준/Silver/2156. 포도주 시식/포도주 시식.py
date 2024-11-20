import sys
input = sys.stdin.readline

n = int(input())
w = []
for _ in range(n):
    w.append(int(input()))
dp = [0]*n
if n == 1:
    print(w[0])
elif n == 2:
    print(w[0]+w[1])
elif n >= 3:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    dp[2] = max(dp[1], w[0]+w[2], w[1]+w[2])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+w[i], dp[i-3]+w[i-1]+w[i])
    print(max(dp))