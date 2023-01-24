from collections import deque

def bfs():
    queue = deque()
    for redTomato in redTomatoList:#익은토마토의 좌표를 큐에 append.
        queue.append(redTomato)
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz,nx,ny))

m, n, h = map(int,input().split())
graph = []
for _ in range(h):#토마토 정보를 3차원으로 저장
    graph.append([list(map(int,input().split())) for _ in range(n)])
redTomatoList = [(i,j,k) for i in range(h) for j in range(n) for k in range(m) if graph[i][j][k] == 1]#익은토마토가 있는 좌표
dx,dy,dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
bfs()
result = [graph[i][j][k] for i in range(h) for j in range(n) for k in range(m)]#3차원의 리스트 값들을 1차원의 리스트값에 다 넣어줌
print(-1 if 0 in result else max(result)-1)#안익은토마토가 있으면 -1, 아니면 최대값-1