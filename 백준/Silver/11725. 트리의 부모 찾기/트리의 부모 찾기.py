import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
result = [0] * (N+1)

def bfs():
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if result[y] == 0:
                result[y] = x
                queue.append(y)
bfs()
result = result[2:]
for i in result:
    print(i)