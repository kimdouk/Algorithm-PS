a,b,n,w = map(int,input().split())
result = []
for x in range(1,n):
    if (a*x) + ((n-x)*b)==w:
        result.append(x)
if len(result)==1:
    print(result[0],n-result[0])
else:
    print(-1)