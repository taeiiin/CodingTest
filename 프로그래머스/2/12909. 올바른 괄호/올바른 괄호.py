def solution(s):
    par = [s[0]]
    for i in range(1, len(s)):
        if s[i] == ')' and par and par[-1] == '(':
            par.pop()
        elif s[i] == '(':
            par.append(s[i]);
    if len(par) == 0:
        answer = True
    else:
        answer = False
    return answer