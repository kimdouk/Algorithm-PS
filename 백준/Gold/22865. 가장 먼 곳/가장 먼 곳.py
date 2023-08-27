import heapq
input = __import__('sys').stdin.readline
n = int(input())
a,b,c = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d,e,l = map(int, input().split())
    graph[d].append((e,l))
    graph[e].append((d,l))
INF = float('inf')

def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = nextDist + dist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
    return distance

a_dist = dijkstra(a)
b_dist = dijkstra(b)
c_dist = dijkstra(c)
result = []
for i in range(1, n+1):
    m = min(a_dist[i], b_dist[i], c_dist[i])
    result.append(m)
idx = max(result)
print(result.index(idx) + 1)