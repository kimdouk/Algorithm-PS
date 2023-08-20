from collections import deque
input = __import__('sys').stdin.readline
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)]
result = [0 for _ in range(n)]
def bfs(start):
    global result
    num = 1
    visited[start] = True
    q = deque([start])
    while q:
        node = q.popleft()
        result[node-1] = num
        num+=1
        for i in sorted(graph[node], reverse=True):
            if not visited[i]:
                visited[i] = True
                q.append(i)
bfs(r)
print(*result, sep='\n')