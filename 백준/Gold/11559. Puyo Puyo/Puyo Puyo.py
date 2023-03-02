from collections import deque
graph = [list(input()) for _ in range(12)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    idx = []
    count = 0
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        idx.append((x,y))
        count +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=12 or ny>=6:continue
            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return count,idx

def down():
    for i in range(6):
        q = []
        for j in range(11,-1,-1):
            if graph[j][i] !='.':
                q.append(graph[j][i])
        for j in range(11,-1,-1):
            if q:
                graph[j][i] = q.pop(0)
            else:
                graph[j][i] = '.'

result = 0
while True:
    flag = 0
    visited = [[False] *6 for _ in range(12)] 
    for i in range(12):
        for j in range(6):
            if graph[i][j] !='.' and not visited[i][j]:
                returnValue = bfs(i,j)
                if returnValue[0]>=4:
                    flag = 1
                    for xidx, yidx in returnValue[1]:
                        graph[xidx][yidx] = '.'
    if flag ==1:
        result +=1
        down()
    if flag==0:
        break

print(result)