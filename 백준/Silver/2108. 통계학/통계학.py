import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))
print(round(sum(li)/n))
li.sort()
print(li[n//2])
d = {}
for i in li:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
x = max(d.values())
y = []
for key, item in d.items():
    if item==x:
        y.append(key)
if len(y)>1:
    print(sorted(y)[1])
else:
    print(y[0])
print(max(li)-min(li))