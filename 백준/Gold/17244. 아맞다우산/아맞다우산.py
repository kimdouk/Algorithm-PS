from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
graph = [list(input()) for _ in range(n)]
data = deque()
dx,dy = [-1,1,0,0],[0,0,-1,1]
mn = float('inf')
for i in range(n):
    for j in range(m):
        if graph[i][j]=='S':
            start = (i,j)
        elif graph[i][j]=='X':
            data.append((i,j))
        elif graph[i][j]=='E':
            end = (i,j)

def bfs(x,y,gx,gy):
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    distance[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        if x==gx and y==gy:return distance[gx][gy]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            if distance[nx][ny]==-1 and graph[nx][ny]!='#':
                distance[nx][ny] = distance[x][y]+1
                q.append((nx,ny))
    # return distance[gx][gy]
if data:
    for i in list(permutations(data,len(data))):
        result = 0
        for j in range(len(i)-1):
            result += bfs(i[j][0],i[j][1],i[j+1][0],i[j+1][1])
        result+= bfs(start[0],start[1],i[0][0],i[0][1])
        result+= bfs(i[-1][0],i[-1][1],end[0],end[1])
        mn = min(mn,result)
else:mn = bfs(start[0],start[1],end[0],end[1])
print(mn)