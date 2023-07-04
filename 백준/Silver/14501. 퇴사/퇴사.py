n = int(input())
task = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
for i in range(n):
    for j in range(task[i][0]+i, n+1):
        if dp[j]<dp[i]+task[i][1]:
            dp[j] = dp[i] + task[i][1]
print(dp[-1])