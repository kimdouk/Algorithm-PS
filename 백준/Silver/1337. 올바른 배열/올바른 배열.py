n = int(input())
data = sorted([int(input()) for _ in range(n)])
mn = float('inf')
for i in range(n):
    cnt = 0
    for j in range(data[i],data[i]+5):
        if j not in data:
            cnt+=1
    mn = min(mn,cnt)
print(mn)