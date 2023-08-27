import heapq
input = __import__('sys').stdin.readline
v,e,p = map(int,input().split())
graph = [[]*(v+1) for _ in range(v+1)]
INF = float('inf')
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
def dijkstra(start):
    distance = [INF for _ in range(v+1)]
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
    return distance
d = dijkstra(1)
a,c = d[p], d[v]
nd = dijkstra(p)
b = nd[v]
if a+b==c:print("SAVE HIM")
else:print("GOOD BYE")