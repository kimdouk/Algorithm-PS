n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0 for _ in range(k)]
for i in coins:
    for j in range(i,k+1):
        dp[j] = dp[j] + dp[j-i]
print(dp[-1])