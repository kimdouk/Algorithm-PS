import heapq
input = __import__('sys').stdin.readline
n, v, e = map(int, input().split())
A,B = map(int, input().split())
team = list(map(int, input().split()))
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = nextDist + dist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))

result = 0
for i in range(n):
    KIST = 0
    FOOD = 0
    INF = 10001
    distances = [INF] * (v+1)
    dijkstra(team[i], distances)
    if distances[A] == INF:
        KIST = -1
    if distances[B] == INF:
        FOOD = -1
    if distances[A] != INF:
        KIST = distances[A]
    if distances[B] != INF:
        FOOD = distances[B]
    result = result + KIST + FOOD
print(result)