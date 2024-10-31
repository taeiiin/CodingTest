def solution(P, S):
    answer = []
    while P:
        cnt = 0
        while P and P[0] >= 100:
            cnt += 1
            P.pop(0)
            S.pop(0)
        P = [P[i] + S[i] for i in range(len(P))]
        if cnt:
            answer.append(cnt)
    return answer