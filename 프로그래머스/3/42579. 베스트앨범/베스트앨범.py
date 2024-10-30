def solution(genres, plays):
    answer = []
    music = {}
    play = {}
    for i in range(len(genres)):
        if genres[i] in music:
            music[genres[i]].append([plays[i], i])
        else:
            music[genres[i]] = [[plays[i], i]]
    for g, p in zip(genres, plays):
        play[g] = play.get(g, 0) + p
    play = sorted(play.items(), key = lambda x: x[1], reverse=True)
    for g in play:
        song = sorted(music[g[0]], key = lambda x:(-x[0], x[1]))
        best = 0
        for s in song:
            answer.append(s[1])
            best += 1
            if best == 2:
                break
    return answer