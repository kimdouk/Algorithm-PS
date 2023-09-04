def dfs(x,y):
    visited[x][y] = True
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:continue
        if not visited[nx][ny] and graph[nx][ny]==1:
            dfs(nx,ny)
    return

input = __import__('sys').stdin.readline
__import__('sys').setrecursionlimit(10**6)
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
while True:
    m,n = map(int,input().split())
    if n==0 and m==0:break
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] ==1:
                cnt+=1
                dfs(i,j)
    print(cnt)