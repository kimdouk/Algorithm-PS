n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(3):
        if j == 0:dp[i][j] = dp[i][j] + min(dp[i-1][j+1],dp[i-1][j+2])
        if j == 2:dp[i][j] = dp[i][j] + min(dp[i-1][j-1],dp[i-1][j-2])
        if j == 1:dp[i][j] = dp[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])
result = []
for i in range(3):
    result.append(dp[-1][i])
print(min(result))