n = int(input())
for i in range(1, n+1):
    i = str(i)
    if '3' in i or '6' in i or '9' in i:
        x = i.count('3') + i.count('6') + i.count('9')
        print('-'*x, sep="", end=" ")
    else:
        print(i, end=" ")