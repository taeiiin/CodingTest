n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
li.sort()
dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if li[j][1] < li[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))