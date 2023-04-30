n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
INF = float('inf')
mn = INF
for j in range(3):
    dp = [[INF]*(3) for _ in range(n)]
    dp[0][j] = data[0][j]
    for i in range(1,n):
        dp[i][0] = data[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = data[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = data[i][2] + min(dp[i-1][0], dp[i-1][1])
    for k in range(3):
        if j!=k:mn = min(mn,dp[-1][k])
print(mn)