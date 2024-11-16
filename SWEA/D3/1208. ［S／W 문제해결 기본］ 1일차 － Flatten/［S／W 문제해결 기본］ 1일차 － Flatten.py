for test_case in range(1, 10 + 1):
    n = int(input())
    box = list(map(int, input().split()))
    for i in range(n):
        x, y = box.index(max(box)), box.index(min(box))
        box[x] -= 1
        box[y] += 1
    print("#%d %d" % (test_case, max(box) - min(box)))