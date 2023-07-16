n = int(input())
data = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if data[i]>data[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))