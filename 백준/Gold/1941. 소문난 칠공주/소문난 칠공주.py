from collections import deque
graph = [input() for _ in range(5)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
result = []
total = 0

def bfs(result):
    visited = [[True for _ in range(5)] for _ in range(5)]
    for i,j in result:
        visited[i][j] = False
    q = deque([(result[0])])
    visited[result[0][0]][result[0][1]] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                cnt+=1
                q.append((nx,ny))
    if cnt==7:
        return 1
    else:return 0

    
def dfs(depth,start,ycnt):
    global result
    global total
    if ycnt>=4:return
    if depth==7:
        total+=bfs(result)
        return
    for i in range(start,25):
        result.append((i//5,i%5))
        dfs(depth +1, i+1, ycnt+(graph[i//5][i%5]=='Y'))
        result.pop()
dfs(0,0,0)
print(total)