T = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    x = 0
    if m1 == m2:
        x = d2 - d1 + 1
    else:
        x = month[m1] - d1 + 1
        for i in range(m1 + 1, m2):
            x += month[i]
        x += d2
    print("#%d %d" %(test_case, x))