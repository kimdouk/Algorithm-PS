from itertools import permutations
n = int(input())
data = list(map(int,input().split()))
mx = 0
for i in list(permutations(data,n)):
    result = 0
    for j in range(len(i)-1):
        result += abs(i[j]-i[j+1])
    mx = max(mx,result)
print(mx)