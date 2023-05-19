import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
for _ in range(int(input())):
    n,d,c = map(int,input().split())
    distance = [INF for _ in range(n+1)]
    graph = [[]*(n+1) for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    q = []
    heapq.heappush(q,(0,c))
    distance[c] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:continue
        for nextNode, nextDist in graph[node]:
            cost = dist+nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
    result = []
    for i in range(1,n+1):
            if distance[i] != INF:
                result.append(distance[i])
    print(len(result), max(result))