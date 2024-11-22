n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
m.sort(key=lambda x: (x[1], x[0]))
cnt, temp = 1, m[0][1]
for i in range(1, n):
    if m[i][0] >= temp:
        temp = m[i][1]
        cnt += 1
print(cnt)