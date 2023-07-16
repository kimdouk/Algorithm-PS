from itertools import permutations
n,k = map(int,input().split())
kits = list(map(int,input().split()))
permutation = list(permutations(range(n),n))
cnt = 0
for i in permutation:
    kg = 500
    for j in i:
        kg += kits[j]-k
        if kg<500:
            cnt+=1
            break
print(len(permutation)-cnt)