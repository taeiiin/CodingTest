T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    cnt, temp = 0, 0
    for i in range(max(n, m) - min(n, m)+1):
        num = 0
        for j in range(min(n, m)):
            if n < m:
                num += Aj[j] * Bj[j+temp]
            elif m < n:
                num += Aj[j+temp] * Bj[j]
            else:
                num += Aj[j] * Bj[j]
        if num > cnt:
            cnt = num
        temp += 1
    print("#%d %d" %(test_case, cnt))