T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    score = []
    unit = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for _ in range(n):
        a, b, c = list(map(int, input().split()))
        m = a*0.35 + b*0.45 + c*0.2
        score.append(m)
    rank = sorted(score, reverse=True)
    print("#%d %s" %(test_case, unit[(rank.index(score[k-1]))//(n//10)]))