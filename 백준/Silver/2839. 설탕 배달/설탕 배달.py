n = int(input())
cnt = 0
while True:
  if n%5==0:
    cnt += n//5
    print(cnt)
    break
  elif n==0:
    print(cnt)
    break
  elif n==1 or n==2:
    print(-1)
    break
  else:
    n -= 3
    cnt += 1