t = []
for i in range(3):
    t.append(int(input()))
if sum(t)!=180:
    print('Error')
t2 = set(t)
if sum(t)==180 and len(t2)==3:
    print('Scalene')
elif sum(t)==180 and len(t2)==2:
    print('Isosceles')
elif sum(t)==180 and len(t2)==1:
    print('Equilateral')