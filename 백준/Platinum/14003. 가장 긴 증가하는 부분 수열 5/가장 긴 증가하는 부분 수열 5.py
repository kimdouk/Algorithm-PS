from bisect import bisect_left
n = int(input())
data = list(map(int,input().split()))
dp = [data[0]]
result = [(data[0],0)]
for i in range(1,n):
    if dp[-1]<data[i]:
        result.append((data[i],len(dp)))
        dp.append(data[i])
    else:
        idx = bisect_left(dp,data[i])
        dp[idx] = data[i]
        result.append((data[i],idx))
ans = []
num = len(dp)-1
for i in range(len(result)-1,-1,-1):
    if num == result[i][1]:
        num -=1
        ans.append(result[i][0])
print(len(ans))
print(*ans[::-1])