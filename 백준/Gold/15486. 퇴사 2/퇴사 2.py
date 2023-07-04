import sys
input = sys.stdin.readline
n = int(input())
t,p = [0],[0]
for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)
dp = [0 for _ in range(n+2)]

for i in range(1,n+1):
    dp[i] = max(dp[i], dp[i-1])
    if i+t[i]<=n+1:
        if dp[i+t[i]]< dp[i] + p[i]:
            dp[i+t[i]] = dp[i] + p[i]
print(max(dp))