T = int(input())
for test_case in range(1, T + 1):
    a, b = map(str, input().split())
    lcs = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    print("#%d %d" % (test_case, lcs[len(a)][len(b)]))