import heapq
input = __import__('sys').stdin.readline
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = nextDist + dist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
dijkstra(x)
result = []
for i in range(n+1):
    if distance[i]==k:result.append(i)
if not result:print(-1)
else:print(*result, sep='\n')