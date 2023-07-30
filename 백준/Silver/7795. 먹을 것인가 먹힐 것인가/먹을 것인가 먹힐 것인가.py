from bisect import bisect_left
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    result = 0
    for i in a:
        result+=bisect_left(b,i)
    print(result)