from itertools import product
n, m = map(int, input().split())
pro = [[*i] for i in product(range(1, n+1), repeat=m)]
pro.sort()
for p in pro:
    print(*p, sep=" ")