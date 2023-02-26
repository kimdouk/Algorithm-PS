from itertools import permutations
a, b = input().split()
result = []
for i in list(permutations(a,len(a))):
    if i[0] !='0':
        num = int(''.join(i))
        if num < int(b):
            result.append(num)
print(max(result) if len(result)!=0 else -1)