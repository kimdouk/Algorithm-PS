n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
idx = min(n,m)
result = 0
for k in range(idx):
    for i in range(n-k):
        for j in range(m-k):
            if graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                result =k+1
print(result**2)