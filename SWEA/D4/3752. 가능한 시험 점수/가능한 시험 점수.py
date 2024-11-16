T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    p = list(map(int, input().split()))
    result = [0]*(sum(p)+1)
    result[0] = 1
    score = [0]
    for i in p:
        temp = score[:]
        for j in temp:
            if result[i+j] == 0:
                result[i+j] = 1
                score.append(i+j)
    print(f"#{test_case} {len(score)}")