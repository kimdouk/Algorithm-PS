for _ in range(int(input())):
    cnt = 0
    n,d = map(int,input().split())
    for _ in range(n):
        v,f,c = map(int,input().split())
        if d<=v*(f/c):cnt+=1
    print(cnt)