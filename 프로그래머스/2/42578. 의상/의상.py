def solution(clothes):
    hashmap = {}
    for c in clothes:
        hashmap[c[1]] = hashmap.get(c[1], 0) + 1
    answer = 1
    for h in hashmap:
        answer *= (hashmap[h] + 1)
    return answer - 1