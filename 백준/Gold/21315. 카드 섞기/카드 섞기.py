import sys
def dfs(deck,k):
    if k == -1:
        return deck
    return dfs(deck[-(2**k):],k-1) + deck[:-(2**k)]

n = int(input())
deck = [i for i in range(1,n+1)]
ans = list(map(int,input().split()))
k = 0
for i in range(1,n):
    if 2**i>=n:
        k = i-1
        break

# 1,1 1,2 2,1 2,2
for i in range(1,k+1):
    for j in range(1,k+1):
        if ans == (dfs(dfs(deck,i),j)):
            print(i,j)
            sys.exit()