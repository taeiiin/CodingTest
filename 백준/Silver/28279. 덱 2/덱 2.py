from collections import deque
import sys
n = int(sys.stdin.readline())
d = deque()
for _ in range(n):
    m = sys.stdin.readline().strip()
    if m=='3':
        if d: print(d.popleft())
        else: print(-1)
    elif m=='4':
        if d: print(d.pop())
        else: print(-1)
    elif m=='5':
        print(len(d))
    elif m=='6':
        if not d: print(1)
        else: print(0)
    elif m=='7':
        if d: print(d[0])
        else: print(-1)
    elif m=='8':
        if d: print(d[-1])
        else: print(-1)
    else:
        a, b = map(int, m.split())
        if a==1: d.appendleft(b)
        else: d.append(b)