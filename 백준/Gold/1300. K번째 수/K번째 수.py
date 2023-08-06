n = int(input())
k = int(input())
st,end = 1,k
while st<=end:
    mid = (st+end)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i,n)
    if cnt>=k:
        ans = mid
        end = mid-1
    else:
        st = mid+1
print(ans)