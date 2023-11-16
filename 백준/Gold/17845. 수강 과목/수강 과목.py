input = __import__('sys').stdin.readline
n,k = map(int,input().split())
data = [[0,0]] + [list(map(int,input().split())) for _ in range(k)]
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(1,k+1):
    for j in range(1,n+1):
        value = data[i][0]
        time = data[i][1]
        if j<time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + value)
print(dp[-1][-1])