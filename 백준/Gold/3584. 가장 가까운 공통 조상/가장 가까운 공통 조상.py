sys = __import__('sys').stdin.readline
def find(parent,x):
    arr = [x]
    while parent[x]:
        arr.append(parent[x])
        x = parent[x]
    return arr

for _ in range(int(input())):
    n = int(input())
    parent = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    a,b = map(int,input().split())
    alist = find(parent,a)
    blist = find(parent,b)
    flag  =0
    for i in alist:
        for j in blist:
            if i==j:
                flag = 1
                print(i)
            if flag:break
        if flag:break