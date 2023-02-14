from itertools import permutations
n,m=map(int,input().split())
data = sorted(list(map(int,input().split())))
result = permutations(data,m)
for i in result:
    print(*i)