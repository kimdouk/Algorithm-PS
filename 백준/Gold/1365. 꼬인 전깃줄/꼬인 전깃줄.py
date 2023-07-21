n = int(input())
data = [*map(int,input().split())]
dp = [data[0]]
for i in range(n):
    if dp[-1]<data[i]:
        dp.append(data[i])
    else:
        dp[__import__('bisect').bisect_left(dp,data[i])] = data[i]
print(n-len(dp))