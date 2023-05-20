import heapq
import sys
input = sys.stdin.readline

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
    return distance[d]
    
n,d = map(int,input().split())
INF = float('inf')
graph = [[] for _ in range(d+1)]
distance = [INF for _ in range(d+1)]
for i in range(d):
    graph[i].append((i+1,1))
for _ in range(n):
    a,b,c = map(int,input().split())
    if a>d or b>d:continue
    graph[a].append((b,c))

print(dijkstra(0))