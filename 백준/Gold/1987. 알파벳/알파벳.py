import sys
# sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
graph = [input() for _ in range(n)]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
check = [0 for _ in range(len(alpha))]
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,cnt):
    global result
    
    result = max(result,cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:continue
        if not check[alpha.index(graph[nx][ny])]:
            check[alpha.index(graph[nx][ny])] =1
            dfs(nx,ny,cnt+1)
            check[alpha.index(graph[nx][ny])] =0

check[alpha.index(graph[0][0])] =1
dfs(0,0,1)
print(result)