import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def bfs(start,dist):
    queue = deque([(start,dist)])
    visited[start] = True

    while queue:
        x,dist = queue.popleft()
        distance[x] = dist
        for nextNode,nextDist in graph[x]:
            if not visited[nextNode]:
                cost = nextDist+dist
                queue.append((nextNode,cost))
                visited[nextNode] = True
    return max(distance)
result = -1
for i in range(1,n+1):
    distance = [0] *(n+1)
    visited = [False] *(n+1)
    result = max(result, bfs(i,0))
print(result)