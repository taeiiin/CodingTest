import sys
import heapq

n = int(sys.stdin.readline())
minh, maxh = [], []
for i in range(n):
    x = int(sys.stdin.readline())
    if len(maxh) == len(minh):
        heapq.heappush(maxh, -x)
    else:
        heapq.heappush(minh, x)
    if minh and -maxh[0] > minh[0]:
        a = -heapq.heappop(maxh)
        b = heapq.heappop(minh)
        heapq.heappush(maxh, -b)
        heapq.heappush(minh, a)
    print(-maxh[0])