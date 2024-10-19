T = int(input())
for test_case in range(1, T + 1):
	a, b, n = map(int, input().split())
	result = 0
	while a<=n and b<=n:
		if a>b:
			b += a
		else:
			a += b
		result += 1
	print(result)