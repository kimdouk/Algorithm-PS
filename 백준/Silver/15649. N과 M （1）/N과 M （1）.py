from itertools import permutations
n,m = map(int,input().split())
data = [i for i in range(1,n+1)]
result = permutations(data,m)
for i in result:
    print(*i)