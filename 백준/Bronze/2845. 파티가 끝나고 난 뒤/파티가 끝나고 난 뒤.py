a,b = map(int,input().split())
sm = a*b
num = list(map(int,input().split()))
for i in num:print(i-sm, end=' ')