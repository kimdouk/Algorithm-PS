n = int(input())
m = int(input())
data = sorted(list(map(int,input().split())))
l,r = 0,n-1
result = 0
while l<r:
    mid = data[l]+data[r]
    if mid<m:l+=1
    elif mid>m:r-=1
    else:
        result+=1
        r-=1
print(result)