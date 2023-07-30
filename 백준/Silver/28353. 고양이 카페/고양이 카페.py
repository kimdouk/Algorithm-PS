n,k = map(int,input().split())
weight = sorted(list(map(int,input().split())))
l,r = 0,n-1
result = 0
while l<r:
    mid = weight[l]+weight[r]
    if mid>k:r-=1
    else:
        result+=1
        l+=1
        r-=1
print(result)