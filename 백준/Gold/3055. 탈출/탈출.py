from collections import deque
from copy import deepcopy

def bfs_water(graph,water_idx):
    q = deque()
    
    for x,y in water_idx:
        q.append((x,y))
        time[x][y] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:continue
            if graph[nx][ny] =='.':
                graph[nx][ny] = '#'
                time[nx][ny] = time[x][y] + 1
                q.append((nx,ny))

def bfs_hedgehog(x,y):
    graph[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=r or ny>=c:continue
            # if graph[nx][ny] == 'D':
            #     graph[nx][ny] = graph[x][y]+1
            elif graph[nx][ny] =='.' or graph[nx][ny] =='D':
                if graph[x][y]+1< time[nx][ny]:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx,ny))
            
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
water_idx = []
INF = float('inf')
time = [[INF for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if graph[i][j]=='D':ans_x,ans_y = i,j
        elif graph[i][j]=='*':water_idx.append((i,j))
        elif graph[i][j]=='S':
            hedgehog_x,hedgehog_y = i,j

bfs_water(deepcopy(graph),water_idx)
bfs_hedgehog(hedgehog_x,hedgehog_y)
print('KAKTUS' if graph[ans_x][ans_y] =='D' else graph[ans_x][ans_y])