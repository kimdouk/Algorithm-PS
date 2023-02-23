import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dfs(x,y,visited,total):
    if x == y:
        print(total)
        return
    visited[x] = True
    for node,dist in graph[x]:
        if not visited[node]:
            total+=dist
            dfs(node,y,visited,total)
            total-=dist

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
for _ in range(m):
    visited = [False] * (n+1)
    start, end = map(int,input().split())
    dfs(start,end,visited,0)