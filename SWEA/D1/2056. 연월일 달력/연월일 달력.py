T = int(input())
for test_case in range(1, T + 1):
	n = str(input())
	month = int(n[4:6])
	day = int(n[6:8])
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if month in range(1, 13):
		if day in range(1, days[month-1]+1):
			print("#%d %s/%s/%s" %(test_case, n[0:4], n[4:6], n[6:8]))
		else:
			print("#%d -1" %(test_case))
	else:
		print("#%d -1" %(test_case))