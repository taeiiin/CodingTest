n = int(input())
li = list(map(int, input().split()))
r_li = li[::-1]
inc, dec = [1]*n, [1]*n

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if r_li[i] > r_li[j]:
            dec[i] = max(dec[i], dec[j]+1)
dec = dec[::-1]
result = []
for i in range(n):
    result.append(dec[i]+inc[i]-1)
print(max(result))