for test_case in range(1, 11):
    n = int(input())
    b = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        if b[i - 2] < b[i] and b[i - 1] < b[i] and b[i + 1] < b[i] and b[i + 2] < b[i]:
            result += b[i] - max(b[i - 2], b[i - 1], b[i + 1], b[i + 2])
    print("#%d %d" % (test_case, result))