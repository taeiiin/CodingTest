T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    price, j = 0, 0
    for i in li[::-1]:
        if price < i:
            price = i
        else:
            j += price - i
    print("#%d %d" %(test_case, j))