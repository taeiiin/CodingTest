N = int(input())
num = list(map(int, input().split()))
opt = list(map(int, input().split()))
max_num, min_num = -1e9, 1e9
def dfs(dep, total, plus, minus, mul, div):
    global max_num, min_num
    if dep == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    if plus:
        dfs(dep + 1, total + num[dep], plus - 1, minus, mul, div)
    if minus:
        dfs(dep + 1, total - num[dep], plus, minus - 1, mul, div)
    if mul:
        dfs(dep + 1, total * num[dep], plus, minus, mul - 1, div)
    if div:
        dfs(dep + 1, int(total/num[dep]), plus, minus, mul, div - 1)
dfs(1, num[0], opt[0], opt[1], opt[2], opt[3])
print(max_num, min_num, sep='\n')