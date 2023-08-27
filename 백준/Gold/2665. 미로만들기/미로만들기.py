import heapq
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False for _ in range(n)] for _ in range(n)]
def dijkstra():
    q = []
    heapq.heappush(q,(0,0,0))
    while q:
        a,x,y = heapq.heappop(q)
        if x==n-1 and y==n-1:
            print(a)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if visited[nx][ny]:continue
            visited[nx][ny] = True
            if graph[nx][ny] == 1:
                heapq.heappush(q,(a,nx,ny))
            else:
                heapq.heappush(q,(a+1,nx,ny))
dijkstra()