import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
city = list(map(int,input().split()))
connect = [(i+1,j+1)for i in range(n) for j in range(n) if graph[i][j] ==1]
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for a,b in connect:
    union_parent(a,b)
result = set()
for i in city:
    result.add(find_parent(parent,parent[i]))
print('YES' if len(result)==1 else 'NO')