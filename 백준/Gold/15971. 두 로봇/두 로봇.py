import heapq
import sys

input = sys.stdin.readline
n,x,y = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
INF = float('inf')

def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = dist+nextDist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
    return distance

distA = dijkstra(x)
distB = dijkstra(y)
result = INF
for i in range(1,len(distA)):
    for j in graph[i]:
        result = min(result,distA[i]+distB[j[0]])
for i in range(1,len(distA)):
    result = min(result, distA[i] + distB[i])
print(0 if n==1 else result)