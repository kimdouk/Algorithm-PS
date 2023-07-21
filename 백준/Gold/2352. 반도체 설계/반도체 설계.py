from bisect import bisect_left
n = int(input())
data = list(map(int,input().split()))
dp = [data[0]]
for i in range(n):
    if dp[-1]<data[i]:
        dp.append(data[i])
    else:
        idx = bisect_left(dp,data[i])
        dp[idx] = data[i]
print(len(dp))