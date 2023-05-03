import sys
input = sys.stdin.readline
n,m = map(int,input().split())
INF = float('inf')
graph = [[INF]*(n+1) for _ in range(n+1)]
nodeToNode = [[-1]*(n+1) for _ in range(n+1)]

def shortest_time(start):
    shortest = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            # if i==start or j==start:continue
            if nodeToNode[i][j]!=-1:#노드와 노드사이에 간선이 존재
                remainNode = nodeToNode[i][j] - (graph[start][j] - graph[start][i])
                if remainNode>=0:
                    now_time = remainNode/2 + graph[start][j]
                    shortest = max(shortest,now_time)
    return shortest
    

for _ in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b]>c:
        graph[a][b] = c
        graph[b][a] = c
    if nodeToNode[a][b]<c:#노드에서 노드의 최대 간선 길이
        nodeToNode[a][b] = c
        nodeToNode[b][a] = c

for i in range(1,n+1):
    graph[i][i] = 0
for k in range(1,n+1):#플로이드
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = INF
for i in range(1,n+1):
    result = min(result,shortest_time(i))
print(result)