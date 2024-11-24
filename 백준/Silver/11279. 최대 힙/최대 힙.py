import sys
import heapq as hq

n = int(input())
heap = []
for _ in range(n):
    m = int(sys.stdin.readline())
    if m:
        hq.heappush(heap, (-m, m))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)