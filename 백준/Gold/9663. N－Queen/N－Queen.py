def is_queen(x):
    for i in range(x):
        if c[x] == c[i] or abs(c[x]-c[i]) == abs(x-i):
            return False
    return True
def queens(x):
    global y
    if x == n:
        y += 1
        return
    else:
        for i in range(n):
            c[x] = i
            if is_queen(x):
                queens(x+1)
n = int(input())
y = 0
c = [0] * n
queens(0)
print(y)