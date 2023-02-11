n,s = map(int,input().split())
data = list(map(int,input().split()))
end = 0
total = data[0]
mn = float('inf')
for start in range(n):
    while end<n and total<s:
        end+=1
        if end!=n:total+=data[end]
    if end==n:break
    mn = min(mn,end-start+1)
    total -= data[start]
print(0 if mn==float('inf') else mn)