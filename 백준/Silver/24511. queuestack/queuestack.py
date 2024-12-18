import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
m = int(input())
C = deque(map(int, input().split()))
q = deque()
for i in range(n):
    if A[i]==0:
        q.append(B[i])
else:
    if q==[]:
        print(*C)
for i in range(m):
    q.appendleft(C[i])
    print(q.pop(), end=' ')