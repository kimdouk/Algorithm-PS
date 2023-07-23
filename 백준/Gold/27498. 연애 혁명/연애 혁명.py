
import sys
input = sys.stdin.readline
def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
edges = []
parent = [i for i in range(n+1)]
result,sm = 0,0
for _ in range(m):
    a,b,cost,isCouple = map(int,input().split())
    if isCouple==0:
        sm+=cost
        edges.append((cost,a,b))
    elif isCouple==1:
        union(parent,a,b)

edges.sort(reverse=True)

for edge in edges:
    cost,a,b = edge
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        result+=cost
print(sm-result)