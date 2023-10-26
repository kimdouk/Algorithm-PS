from itertools import permutations
n = input()
result = []
for i in list(permutations(n,len(n))):
    result.append(''.join(i))
result = sorted(list(set(result)), reverse=True)
print(0 if result.index(n)==0 else result[result.index(n)-1])