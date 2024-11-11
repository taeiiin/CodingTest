def h(n, x, y, m):
  if n==1:
    print(x, y)
    return
  else:
    h(n-1, x, m, y)
    print(x, y)
    h(n-1, m, y, x)
n = int(input())
print(2**n-1)
h(n, 1, 3, 2)