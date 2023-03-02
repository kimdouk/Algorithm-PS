t = int(input())
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a!=b:
        parent[b] = a
        count[a] += count[b]

for _ in range(t):
    f = int(input())
    parent = dict()
    count = dict()
    for i in range(f):
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union_parent(a,b)
        print(count[find_parent(parent,a)])