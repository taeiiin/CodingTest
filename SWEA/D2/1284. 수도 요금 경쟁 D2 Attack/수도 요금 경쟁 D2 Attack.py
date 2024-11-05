T = int(input())
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    if w <= r:
        c = q
    else:
        c = q + (w-r)*s
    print("#%d %d" %(test_case, min(p*w, c)))