import sys
input = sys.stdin.readline
v,e = map(int,input().split())
INF = float('inf')
graph = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c
for i in range(1,v+1):
    for j in range(1,v+1):
        if i==j:graph[i][j]=0
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = INF
for i in range(1,v+1):
    for j in range(1,v+1):
        if i!=j:result = min(result, graph[i][j] + graph[j][i])
print(-1 if result == INF else result)