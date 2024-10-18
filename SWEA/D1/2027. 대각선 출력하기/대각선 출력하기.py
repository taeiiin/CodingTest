x = 0
li = ['+']*5
for i in range(5):
	li[x] = '#'
	print(''.join(li))
	li[x] = '+'
	x += 1