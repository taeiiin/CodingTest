T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    num = set(li)
    result, x = 0, 0
    for i in num:
        if li.count(i) > x:
            result, x = i, li.count(i)
    print("#%d %d" %(n, result))