import sys
n = int(sys.stdin.readline())
cnt = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num==0:
        del cnt[-1]
    else:
        cnt.append(num)
    m = num
print(sum(cnt))