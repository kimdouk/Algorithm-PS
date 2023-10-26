from itertools import combinations
from collections import defaultdict
data = [input() for _ in range(3)]
k = int(input())
cnt = defaultdict(int)
result = []
for st in data:
    for i in list(combinations(st,k)):
        cnt[''.join(i)]+=1
for i,j in cnt.items():
    if j>=2:result.append(i)

if result:
    print(*sorted(result),sep='\n')
else:
    print(-1)