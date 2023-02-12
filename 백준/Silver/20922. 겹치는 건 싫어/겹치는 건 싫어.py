n,k=map(int,input().split())
data = list(map(int,input().split()))
end, mx=0,0
check = [0] * (max(data)+1)
for start in range(n):
    while end<n and check[data[end]]<k:
        check[data[end]]+=1
        end+=1
    mx = max(mx,end-start)
    check[data[start]]-=1
    if end ==n:break
print(mx)