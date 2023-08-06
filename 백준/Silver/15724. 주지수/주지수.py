input = __import__('sys').stdin.readline
n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(m+1):
        prefix_sum[i][j] = prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+data[i-1][j-1]
for _ in range(int(input())):
    i,j,x,y = map(int,input().split())
    print(prefix_sum[x][y] - prefix_sum[x][j-1] - prefix_sum[i-1][y]+prefix_sum[i-1][j-1])