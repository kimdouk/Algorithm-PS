def dfs(x,y):
    if x == n-1 and y ==m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]<graph[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(m) for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
print(dfs(0,0))