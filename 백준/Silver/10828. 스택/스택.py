from collections import deque
import sys
n = int(sys.stdin.readline())
st = deque()
for _ in range(n):
    m = sys.stdin.readline().rstrip()
    if m == "pop":
        if st:
            print(st.pop())
        else:
            print(-1)
    elif m == "size":
        print(len(st))
    elif m == "empty":
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif m == "top":
        if st:
            print(st[-1])
        else:
            print(-1)
    else:
        a, b = map(str, m.split())
        st.append(int(b))