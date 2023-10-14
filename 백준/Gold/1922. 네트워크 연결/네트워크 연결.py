__import__('sys').stdin.readline
def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:parent[a] = b

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edges = []
result = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()
for cost,a,b in edges:
    if find(parent,a)!=find(parent,b):
        union(a,b)
        result+=cost
print(result)