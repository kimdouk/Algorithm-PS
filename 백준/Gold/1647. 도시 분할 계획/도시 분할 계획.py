import sys
input = sys.stdin.readline

def find(parent,x):
    if x!=parent[x]:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:parent[b] = a
    else:parent[a] = b

n,m = map(int,input().split())
edges,result = [],[]
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

for cost,a,b in edges:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result.append(cost)
print(sum(result[:-1]))