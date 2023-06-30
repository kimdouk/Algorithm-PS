from itertools import combinations
num = [int(input()) for _ in range(9)]
for a in list(combinations(num,7)):
    if sum(a)==100:
        print(*a,sep='\n')
        break