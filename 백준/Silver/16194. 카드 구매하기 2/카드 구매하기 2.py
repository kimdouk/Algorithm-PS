n = int(input())
dp = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    mn = float('inf')
    for j in range((i//2)+1):
        mn = min(mn,dp[j]+dp[i-j])
    dp[i] = mn
print(dp[-1])