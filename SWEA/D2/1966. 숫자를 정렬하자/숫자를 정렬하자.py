T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    num = sorted(list(map(int, input().split())))
    print("#%d" %test_case, *num)