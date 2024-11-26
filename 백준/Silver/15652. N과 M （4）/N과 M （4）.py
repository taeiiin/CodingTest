from itertools import combinations_with_replacement
n, m = map(int, input().split())
comb = [[*i] for i in combinations_with_replacement(range(1, n+1), m)]
comb.sort()
for c in comb:
    print(*c, sep=" ")