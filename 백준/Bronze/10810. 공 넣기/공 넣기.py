n,m = map(int,input().split())
basket = [0]*(n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    for idx in range(i,j+1):
        basket[idx] = k
print(*basket[1:])