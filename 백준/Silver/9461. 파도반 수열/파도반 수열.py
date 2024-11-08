import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    p = [1] * n
    if n < 4:
        print(1)
    else:
        i = 3
        while i < n:
            p[i] = p[i-2] + p[i-3]
            i += 1
        print(p[n-1])