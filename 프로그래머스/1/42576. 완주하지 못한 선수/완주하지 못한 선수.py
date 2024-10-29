def solution(participant, completion):
    hashD = {}
    sumHash = 0
    for i in participant:
        hashD[hash(i)] = i
        sumHash += hash(i)
    for j in completion:
        sumHash -= hash(j)
    return hashD[sumHash]