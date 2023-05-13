import sys

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a>b:parent[a] = b
    else:parent[b] = a

input = sys.stdin.readline
n, m = map(int,input().split())
parent = [i for i in range(n)]
result = 0
for i in range(m):
    a,b = map(int,input().split())
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
    else:
        result = i+1
        break
print(result)