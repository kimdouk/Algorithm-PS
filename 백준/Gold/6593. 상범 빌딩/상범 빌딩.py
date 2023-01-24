from collections import deque

def bfs(z,x,y):
    visited[z][x][y] = 0
    queue = deque([(z,x,y)])
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=r or ny>=c or nz>=l:continue
            if (graph[nz][nx][ny] !='#' and visited[nz][nx][ny] == -1) :
                visited[nz][nx][ny] = visited[z][x][y] + 1
                queue.append((nz, nx, ny))


while True:
    l, r, c = map(int,input().split())
    if l==r==c==0:break

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]
    graph = []
    for i in range(l):
        graph.append([list(input()) for _ in range(r)])
        trash = input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':z,x,y = i,j,k
                if graph[i][j][k] == 'E':ez,ex,ey = i,j,k
    visited = [[[-1]*c for _ in range(r)]for _ in range(l)]
    bfs(z,x,y)
    result = visited[ez][ex][ey]
    print("Trapped!" if result == -1 else "Escaped in "+ str(result) +" minute(s)." )