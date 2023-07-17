input = __import__('sys').stdin.readline
n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
result = [float('inf') for _ in range(n)]
for i in range(n):
    for j in range(n):
        x,y = xy[i][0], xy[j][1]
        temp = []
        for cx,cy in xy:
            temp.append(abs(cx-x) + abs(cy-y))
        temp.sort()
        sm = 0
        for k in range(n):
            sm+=temp[k]
            result[k] = min(result[k],sm)
print(*result)