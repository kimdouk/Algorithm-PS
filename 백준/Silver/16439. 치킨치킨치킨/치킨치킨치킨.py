from itertools import combinations
n,m = map(int,input().split())
prefer = [list(map(int,input().split())) for _ in range(n)]
possible = list(combinations(range(m),3))
result = []
for i,j,k in possible:
    mx=0
    for idx in range(n):
        mx+=max(prefer[idx][i],prefer[idx][j],prefer[idx][k])
    result.append(mx)
print(max(result))