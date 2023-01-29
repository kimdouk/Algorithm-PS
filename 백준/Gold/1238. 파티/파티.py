import sys
import heapq

input = sys.stdin.readline
n, m, x = map(int,input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start): # start로부터 출발하여 특정노드까지 걸리는 최소 소요시간
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

backfrom_x = dijkstra(x) #x에서 집으로 오는 최소 시간
roundTrip= [] # 왕복소요시간
for i in range(1,n+1): # 집에서 x로 가는 최소시간 + x에서 집으로 오는 최소시간
    roundTrip.append(dijkstra(i)[x] + backfrom_x[i])
print(max(roundTrip)) #N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간