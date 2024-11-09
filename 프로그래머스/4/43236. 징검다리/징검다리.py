def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    rocks.append(distance)
    while left <= right:
        mid = (left+right)//2
        d = 0
        prev = 0
        for r in rocks:
            dist = r - prev
            if dist < mid:
                d += 1
                if d > n:
                    break
            else:
                prev = r
        if d > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer