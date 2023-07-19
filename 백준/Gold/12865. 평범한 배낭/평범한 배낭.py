input = __import__('sys').stdin.readline
n,k = map(int,input().split())
bag = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if bag[i][0]>j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-bag[i][0]] + bag[i][1])
print(knapsack[n][-1])