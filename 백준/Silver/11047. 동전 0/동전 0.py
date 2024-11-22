n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
num = 0
for i in a:
    if i <= k:
        num += k//i
        k -= (k//i)*i
print(num)