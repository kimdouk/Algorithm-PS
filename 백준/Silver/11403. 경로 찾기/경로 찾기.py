__import__('sys').stdin.readline
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j]==1:graph[i].append(j)
result = [[0 for _ in range(n)] for _ in range(n)]

def dfs(s,vis):
    for i in graph[s]:
        if not vis[i]:
            vis[i] = True
            dfs(i,vis)
for i in range(n):
    vis = [False for _ in range(n)]
    dfs(i,vis)
    for j in range(n):
        if vis[j]:result[i][j]=1
for i in result:
    print(*i)