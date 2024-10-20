T = int(input())
for test_case in range(1, T + 1):
	n = str(input())
	for i in range(1, 10):
		if n[:i] == n[i:2*i]:
			print("#%d %d" %(test_case, i))
			break
