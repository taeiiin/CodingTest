import sys
input = sys.stdin.readline

s = int(input())
p = [0]*(s+1)
dp = [0]*(s+1)
for i in range(1, s+1):
    p[i] = int(input())
for i in range(1, s+1):
    if i==1:
        dp[i] = p[i]
    elif i==2:
        dp[i] = p[i] + p[i-1]
    else:
        dp[i] = max(dp[i-3]+p[i]+p[i-1], dp[i-2]+p[i])
print(dp[s])