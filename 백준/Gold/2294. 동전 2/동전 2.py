n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
INF = float('inf')
dp = [0] + [INF for _ in range(k)]
for i in coins:
    for j in range(i,k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
print(-1 if dp[-1]==INF else dp[-1])