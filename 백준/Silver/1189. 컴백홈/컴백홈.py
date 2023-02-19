r,c,k = map(int,input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(start,end,distance):
    global result
    visited[start][end] = True
    if start==0 and end ==c-1:
        if distance==k:
            result +=1
        return
    x,y = start,end
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=r or ny>=c:continue
        if graph[nx][ny] =='.' and not visited[nx][ny]:
            dfs(nx,ny,distance+1)
            visited[nx][ny] = False
dfs(r-1,0,1)
print(result)