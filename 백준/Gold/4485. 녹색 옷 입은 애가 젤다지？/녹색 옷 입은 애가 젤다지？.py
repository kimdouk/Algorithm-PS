import heapq
def dijkstra():
    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0] = 0

    while q:
        cost,x,y = heapq.heappop(q)
        if x==n-1 and y == n-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:continue
            if cost+graph[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = cost+graph[nx][ny]
                heapq.heappush(q,(distance[nx][ny],nx,ny))

cnt = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    n = int(input())
    if n==0:break
    INF = float('inf')
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF for _ in range(n)] for _ in range(n)]
    dijkstra()
    print(f'Problem {cnt}: {distance[-1][-1]}')
    cnt+=1