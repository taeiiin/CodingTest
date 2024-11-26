from itertools import permutations
n, m = map(int, input().split())
comb = [[*i] for i in permutations(range(1, n+1), m)]
comb.sort()
for c in comb:
    print(*c, sep=" ")