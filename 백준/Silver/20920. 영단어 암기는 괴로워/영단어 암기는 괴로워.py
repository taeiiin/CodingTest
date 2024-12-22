import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for _ in range(n):
	eng = input().strip()
	if len(eng) < m:
		continue
	if eng in d:
		d[eng] += 1
	else:
		d[eng] = 1
d = sorted(d.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
for i in d:
    print(i[0])