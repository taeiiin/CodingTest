T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test_case in range(1, T + 1):
    n = int(input())
    num = [0]*8
    a = 0
    while n > 0 and a < 8:
        if money[a] > n:
            a += 1
        else:
            n -= money[a]
            num[a] += 1
    print("#%d" %test_case)
    print(*num, sep=' ')