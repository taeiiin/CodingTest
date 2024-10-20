T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flies = []
    for _ in range(n):
        flies.append(list(map(int, input().split())))
    x = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            y = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    y += flies[a][b]
            if x < y:
                x = y
    print("#%d %d" %(test_case, x))