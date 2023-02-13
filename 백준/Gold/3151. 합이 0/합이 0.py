import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
ability = sorted(list(map(int,input().split())))
result = 0
counter = Counter(ability)
for i in range(n):
    target = -(ability[i])
    left = i+1
    right = n-1
    while left<right:
        ability_sum = ability[left] + ability[right]
        if ability_sum == target:
            if ability[left] == ability[right]: # -4 2 2 2 2
                result +=(right-left)
            elif ability[left]!=ability[right]: # -2 0 1 2 2 
                result +=(counter[ability[right]])
            left+=1
        elif ability_sum>target:right-=1
        elif ability_sum<target:left+=1
print(result)