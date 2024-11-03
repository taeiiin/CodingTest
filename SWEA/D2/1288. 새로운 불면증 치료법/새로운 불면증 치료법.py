T = int(input())
num = [i for i in range(10)]
for test_case in range(1, T + 1):
    n = int(input())
    li = [0 for _ in range(10)]
    x = 0
    while sum(li) != 10:
        x += 1
        for i in str(n*x):
            li[int(i)] = 1
    print("#%d %d" %(test_case, n*x))