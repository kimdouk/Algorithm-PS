import sys
import heapq
input = sys.stdin.readline

def dijkstra(x,y):
    q = []
    distance[x][y] = 0
    heapq.heappush(q,(0,x,y))
    while q:
        dist,x,y = heapq.heappop(q)
        if dist>distance[x][y]:continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:continue
            cost = dist + graph[nx][ny]
            if cost<distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(distance[nx][ny], nx,ny))
    return distance[-1][-1]
        
m,n = map(int,input().split())
INF = float('inf')
graph = [list(map(int,input().strip())) for _ in range(n)]
distance = [[INF]*(m) for _ in range(n)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
print(dijkstra(0, 0))