# 시간 초과로 인해 이분탐색을 쓰는 LIS
# 시간복잡도는 O(nlogn) 
# 기본 11053 문제 경우 n^2이지만 12015는 n개를 돌면서(n) n보다 크거타 같은 원소를 찾아주기(logn)만 하면된다.
# 길이는 같으나 원소는 LIS와 다를 수 있음
# LIS2 (이분탐색을 이용한 계산)

from bisect import bisect_left
n = int(input())
data = list(map(int,input().split()))
dp = [0]

for i in range(n):
    if data[i]>dp[-1]:
        dp.append(data[i])
    else:
        dp[bisect_left(dp,data[i])] = data[i]
print(len(dp)-1)