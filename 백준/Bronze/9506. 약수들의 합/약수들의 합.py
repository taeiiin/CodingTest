while True:
    n = int(input())
    if n==-1:
        break
    f = []
    for i in range(1, n):
        if n%i==0:
            f.append(i)
    if sum(f) == n:
        print(n,"=",end=" ")
        print(*f,sep=" + ")
    else:
        print("%d is NOT perfect." %n)