T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    v, d = 0, 0
    for _ in range(n):
        m = list(map(int, input().split()))
        if m[0] == 1:
            v += m[1]
        elif m[0] == 2:
            v -= m[1]
            if v < 0:
                v = 0
        d += v
    print("#%d %d" %(test_case, d))