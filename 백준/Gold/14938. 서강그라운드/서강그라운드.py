import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
item = [0] + list(map(int,input().split()))
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:graph[i][j]=0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
for i in range(1,n+1):
    total = 0
    for j in range(1,n+1):
        if graph[i][j]<=m:total+=item[j]
    result = max(result,total)
print(result)