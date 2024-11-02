T = int(input())
num = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    n = int(input())
    cnt = [0]*5
    for i in range(5):
        while n % num[i] == 0:
            cnt[i] += 1
            n = n//num[i]
    print("#%d" %test_case, *cnt)