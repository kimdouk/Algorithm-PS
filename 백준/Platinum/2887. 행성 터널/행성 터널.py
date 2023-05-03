import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if b>a:
        parent[b] = a
    else:parent[a] = b

n = int(input())
xyz = []
parent = [i for i in range(n)]
for i in range(n):
    x,y,z = map(int,input().split())
    xyz.append([x,y,z,i])
    
edges = []
for i in range(3): #시간복잡도 줄이기 위해 가능성있는 경로만 저장
    xyz.sort(key = lambda x:x[i])
    for j in range(1,n):
        edges.append((abs(xyz[j][i] - xyz[j-1][i]), xyz[j][3],xyz[j-1][3]))

edges.sort() #크루스칼, 최소신장트리 MST
result = 0
for cost,a,b in edges:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += cost
print(result)        