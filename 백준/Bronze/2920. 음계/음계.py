li = list(map(int, input().split()))
a, d = 0, 0
for i in range(1, 9):
    if li[i-1] == i:
        a += 1
    elif li[i-1] == 9-i:
        d += 1
if a == 8:
    print("ascending")
elif d == 8:
    print("descending")
else:
    print("mixed")