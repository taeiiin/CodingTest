import sys
n = int(sys.stdin.readline())
for _ in range(n):
    ps = str(sys.stdin.readline().strip())
    vps = []
    for i in range(len(ps)):
        if ps[i]=='(':
            vps.append(ps[i])
        else:
            if len(vps)!=0 and vps[-1]=='(':
                del vps[-1]
            else:
                vps.append(ps[i])
    if len(vps)==0:
        print('YES')
    else:
        print('NO')