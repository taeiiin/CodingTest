import sys, math
li = [True for _ in range(2*123456 + 1)]
li[0], li[1] = False, False
for i in range(2, int(math.sqrt(2*123456))+1):
    if li[i]:
        j = 2
        while i*j<=123456*2:
            li[i*j]=False
            j += 1
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    cnt = 0
    for i in range((n+1), (n*2)+1):
        if li[i]==True:
            cnt += 1
    print(cnt)