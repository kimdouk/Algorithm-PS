#숨바꼭질과 같다.
from collections import deque

def bfs(v):
    queue = deque([v])
    graph[v] = 0

    while queue:
        x = queue.popleft()
        for i in (x+u, x-d):
            nx = i
            if 0<=nx<f and graph[nx] == -1:
                graph[nx] = graph[x] + 1
                queue.append(nx)

f,s,g,u,d = map(int,input().split())
graph = [-1] * f
bfs(s-1)
print(graph[g-1] if graph[g-1] != -1 else "use the stairs")