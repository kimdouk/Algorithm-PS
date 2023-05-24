from copy import deepcopy
n = int(input())
data = list(map(int,input().split()))
dp = deepcopy(data)
for i in range(n):
    for j in range(i):
        if data[i]>data[j]:
            dp[i] = max(dp[i], dp[j]+data[i])
print(max(dp))