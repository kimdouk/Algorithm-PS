n,m = map(int,input().split())
data = [i for i in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    data[i:j+1] = data[j:i-1:-1]
print(*data[1:])