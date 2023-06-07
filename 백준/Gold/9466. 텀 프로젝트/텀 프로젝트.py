import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    global total
    visited[x] = True
    cycle.append(x)
    if not visited[number[x]]:
        dfs(number[x])
    else:
        if number[x] in cycle:
            total += len(cycle[cycle.index(number[x]):])
        return

for _ in range(int(input())):
    n = int(input())
    number = [0]+list(map(int,input().split()))
    visited = [False for _ in range(n+1)]
    total = 0
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-total)