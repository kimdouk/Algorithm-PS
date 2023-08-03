import heapq
input = __import__('sys').stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    info = list(map(int,input().split()))
    for i in range(1,len(info)-1,2):
        graph[info[0]].append((info[i],info[i+1]))
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
            cost = nextDist+dist
            if cost<distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
    return distance
a = dijkstra(1)
print(max(dijkstra(a.index(max(a[1:])))[1:]))