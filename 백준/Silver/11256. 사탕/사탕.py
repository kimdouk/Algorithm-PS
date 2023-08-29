input = __import__('sys').stdin.readline
for _ in range(int(input())):
    j,n = map(int,input().split())
    box = []
    for _ in range(n):
        a,b = map(int,input().split())
        box.append(a*b)
    cnt = 0
    sm = 0
    for i in sorted(box, reverse=True):
        cnt+=1
        sm+=i
        if sm>=j:break
    print(cnt)