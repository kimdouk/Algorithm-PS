for _ in range(int(input())):
    m,n,x,y = map(int,input().split())
    year = x
    ans = -1
    while year<=m*n:
        if (year-y) % n==0:
            ans = year
            break
        year += m
    print(ans)