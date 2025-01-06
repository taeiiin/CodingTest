import sys
input = sys.stdin.readline
N = int(input())
food = []
for i in range(N):
    data = list(input().split())
    food.append(data[1:])
food.sort()
dash = '--'
answer = []
for i in range(N):
    if i == 0:
        for j in range(len(food[i])):
            answer.append(dash * j + food[i][j])
    else:
        idx = 0
        for j in range(len(food[i])):
            if food[i - 1][j] != food[i][j] or len(food[i - 1]) <= j:
                break
            else:
                idx = j + 1
        for j in range(idx, len(food[i])):
            answer.append(dash * j + food[i][j])
for i in answer:
    print(i)