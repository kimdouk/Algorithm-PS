import sys
input = sys.stdin.readline

n,m = map(int,input().split())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,b = map(int,input().split())
    if b==0:
        graph[u][v] = 0
        graph[v][u] = 1
    else:
        graph[u][v] = 0
        graph[v][u] = 0
        
for i in range(1,n+1):graph[i][i]=0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min (graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    a,b  = map(int,input().split())
    print(graph[a][b])