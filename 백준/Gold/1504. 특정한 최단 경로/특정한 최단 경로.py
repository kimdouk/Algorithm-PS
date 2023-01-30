import sys
import heapq

input = sys.stdin.readline
n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int,input().split())
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nextNode, nextDist in graph[now]:
            cost = dist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))
    return distance

# 1번에서 v1 + v1에서 v2 + v2에서 n까지의 최단경로(v1,v2는 반드시 지나야하므로)
result = min(dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n], dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n])
print(-1 if result >= INF else result)