def dfs(n):
    global result
    if n == N:
        result = max(result, int("".join(map(str, li))))
        return
    for i in range(l - 1):
        for j in range(i+1, l):
            li[i], li[j] = li[j], li[i]
            temp = int("".join(map(str, li)))
            if (n, temp) not in v:
                dfs(n+1)
                v.append((n, temp))
            li[j], li[i] = li[i], li[j]

T = int(input())
for test_case in range(1, T + 1):
    num, N = map(int, input().split())
    l, result = len(str(num)), 0
    li, v = list(map(int, str(num))), []
    dfs(0)
    print("#%d %d" % (test_case, result))