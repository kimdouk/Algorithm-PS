import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())
path = [start] * (n+1)
distance = [INF] * (n+1)

def dijkstra(start):
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
                path[nextNode] = now
                heapq.heappush(q, (cost, nextNode))

dijkstra(start)

result = []
visitPath = end
while visitPath != start:
    result.append(visitPath)
    visitPath = path[visitPath]
result.append(start)
print(distance[end],len(result),sep='\n')
print(*result[::-1])