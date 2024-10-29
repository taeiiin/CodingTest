import sys
n = int(sys.stdin.readline())
color = [[0, 0, 0]]
for _ in range(n):
    color.append(list(map(int, sys.stdin.readline().split())))
t = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    t[i][0] = min(t[i-1][1], t[i-1][2]) + color[i][0]
    t[i][1] = min(t[i-1][0], t[i-1][2]) + color[i][1]
    t[i][2] = min(t[i-1][0], t[i-1][1]) + color[i][2]
print(min(t[n][0], t[n][1], t[n][2]))