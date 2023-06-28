n,m,k = map(int,input().split())
x = 0
for i in range(1,m+1):
    if (2*i <= n and i<=m):
        x=i
std = n+m-(3*x)
if std>=k:print(x)
else:print(x-(((k-std-1)//3)+1))