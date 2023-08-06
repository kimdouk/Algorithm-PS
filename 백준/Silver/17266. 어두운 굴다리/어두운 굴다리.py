n = int(input())
m = int(input())
data = list(map(int,input().split()))
mx = 0
for i in range(1,m):
    mx = max(data[i]-data[i-1],mx)
print(max((mx+1)//2, data[0], n-data[-1]))