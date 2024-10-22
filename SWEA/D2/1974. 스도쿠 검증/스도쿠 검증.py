T = int(input())
for test_case in range(1, T + 1):
    n = []
    for _ in range(9):
        n.append(list(map(int, input().split())))
    num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    cnt = 0
    m = list(map(list, zip(*n)))
    for i in n+m:
        if len(set(i).difference(num))==0 and len(num.difference(set(i)))==0:
            pass
        else:
            cnt += 1
            break
    for i in range(9):
        for j in range(9):
            if i%3==0 and j%3==0:
                x = n[i][j:j+3] + n[i+1][j:j+3] + n[i+2][j:j+3]
                if len(set(x).difference(num)) == 0 and len(num.difference(set(x))) == 0:
                    pass
                else:
                    cnt += 1
                    break
    if cnt == 0:
        cnt = 1
    else:
        cnt = 0
    print("#%d %d" %(test_case, cnt))