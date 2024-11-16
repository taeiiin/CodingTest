def is_q(x):
    for i in range(x):
        if c[x] == c[i] or abs(c[x]-c[i]) == abs(x-i):
            return False
    return True

def q(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            c[x] = i
            if is_q(x):
                q(x+1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    c = [0] * n
    q(0)
    print("#%d %d" %(test_case, result))