T = int(input())
for test_case in range(1, T + 1):
	n, m = map(int, input().split())
	if n == m:
		print("#", test_case, " =", sep="")
	elif n > m:
		print("#", test_case, " >", sep="")
	else:
		print("#", test_case, " <", sep="")