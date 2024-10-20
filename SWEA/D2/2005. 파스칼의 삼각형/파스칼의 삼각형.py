T = int(input())
for test_case in range(1, T + 1):
	n = int(input())
	print("#", test_case, sep="")
	result = []
	temp = []
	for i in range(n):
		result.append(1)
		temp.append(1)
		if i < 2:
			pass
		else:
			for j in range(1, len(result)-1):
				temp[j] = result[j-1] + result[j]
		for j in range(len(result)):
			result[j] = temp[j]
		print(' '.join(map(str, result)))