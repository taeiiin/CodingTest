import sys
input = sys.stdin.readline
N = int(input())
li = [list(map(int, input().strip())) for _ in range(N)]

def quad(r, c, n):
    temp = li[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if li[i][j] != temp:
                n = n//2
                return "(" + quad(r, c, n) + quad(r, c + n, n) + quad(r + n, c, n) + quad(r + n, c + n, n) + ")"
    return str(temp)

print(quad(0, 0, N))
