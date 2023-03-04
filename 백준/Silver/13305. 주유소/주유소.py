n = int(input())
dim = list(map(int,input().split()))
cost = list(map(int,input().split()))
result = 0

mincost = cost[0]
for i in range(n-1):
    if mincost > cost[i]:
        mincost = cost[i]
    result += dim[i] * mincost

print(result)