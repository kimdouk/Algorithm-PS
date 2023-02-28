from itertools import combinations
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
chickenHouses = [(i,j) for i in range(n) for j in range(n) if graph[i][j] == 2]
Homes = [(i,j) for i in range(n) for j in range(n) if graph[i][j] ==1]
result = []

for i in list(combinations(chickenHouses,m)):
    summn = 0
    for Home in Homes:
        mn = float('inf')
        for chickenHouse in i:
            mn = min(mn,abs(Home[0]-chickenHouse[0]) + abs(Home[1]-chickenHouse[1]))
        summn += mn
    result.append(summn)
print(min(result))