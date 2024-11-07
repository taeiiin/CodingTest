def solution(sizes):
    w, h = 0, 0
    for x, y in sizes:
        if x < y:
            x, y = y, x
        w = max(w, x)
        h = max(h, y)
    return w*h