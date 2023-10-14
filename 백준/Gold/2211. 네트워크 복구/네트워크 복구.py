import heapq
input = __import__('sys').stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = float('inf')
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
parent = [0 for _ in range(n+1)]
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = nextDist+dist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
                parent[nextNode] = node
dijkstra(1)
print(n-1)
for i in range(2,n+1):
    print(i,parent[i])
