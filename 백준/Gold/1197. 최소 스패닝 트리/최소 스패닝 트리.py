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

v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i] = i

edges,result = [],0
for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

for cost,a,b in edges:#가중치가 낮은 엣지부터
    if find(parent,a) != find(parent,b):#사이클이 아니면
        union(parent,a,b)#합쳐주고
        result += cost#가중치 ++
print(result)