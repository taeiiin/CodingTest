T = int(input())
for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = h1+h2, m1+m2
    if m >= 60:
        m = m - 60
        h += 1
    if h > 12:
        h = h - 12
    print("#%d %d %d" %(test_case, h, m))