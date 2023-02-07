from bisect import bisect_left
n = int(input())
array = list(map(int,input().split()))
array2 = sorted(set(array))
result = []
for i in range(n):
    result.append(bisect_left(array2, array[i]))
print(*result)