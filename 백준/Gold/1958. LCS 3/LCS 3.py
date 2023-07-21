s = [input() for _ in range(3)]
dp = [[[0]*(len(s[2])+1) for _ in range(len(s[1])+1)] for _ in range(len(s[0])+1)]
for i in range(1,len(s[0])+1):
    for j in range(1,len(s[1])+1):
        for k in range(1,len(s[2])+1):
            if s[0][i-1] == s[1][j-1] == s[2][k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[-1][-1][-1])