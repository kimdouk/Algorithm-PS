from itertools import combinations
n, m =map(int,input().split())
data = [i for i in range(1,n+1)]
result = combinations(data,m)
for i in result:
    print(*i)