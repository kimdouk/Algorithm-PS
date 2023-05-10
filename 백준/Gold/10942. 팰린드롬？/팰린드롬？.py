# dp
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for dist in range(n):#dist는 대각선부터 얼마나 떨어져있는지, start는 대각선 요소 갯수
    for start in range(n-dist):
        end = start+dist
        if start == end:dp[start][end]=1
        elif numbers[start] == numbers[end]:
            if start+1 ==end:
                dp[start][end]=1
            elif dp[start+1][end-1]==1:
                dp[start][end] = dp[start+1][end-1]

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])