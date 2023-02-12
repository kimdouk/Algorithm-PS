import sys
from collections import defaultdict
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
belt = [int(input()) for _ in range(n)]
start, end = 0, k-1
dict = defaultdict(int)
result = 0

dict[c]+=1
for i in range(k):
    dict[belt[i]]+=1
while start<n:
    result = max(result,len(dict))
    dict[belt[start]] -=1
    if dict[belt[start]] ==0:del(dict[belt[start]])
    start+=1
    end+=1
    dict[belt[end%n]]+=1
print(result)