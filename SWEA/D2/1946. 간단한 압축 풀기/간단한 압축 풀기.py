T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    doc = ""
    for _ in range(n):
        a, b = input().split()
        doc += a*int(b)
    print("#%d" %test_case)
    for i in range(0, len(doc), 10):
        print(doc[i:i+10])