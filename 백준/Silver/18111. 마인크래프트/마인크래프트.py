import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
graph= []
mn,mx = float('inf'),-1
ans = float('inf')
height = 0
graph = [list(map(int,input().split())) for _ in range(n)]
for block in range(257):
    upcnt,downcnt,result = 0,0,0
    for i in range(n):
        for j in range(m):
            temp = graph[i][j]
            if temp>block:
                downcnt+=(temp-block)
            else:
                upcnt+=(block-temp)
    result+=(downcnt*2)
    tmp=b
    tmp+=downcnt
    if tmp<upcnt:continue
    result+=(upcnt*1)
    tmp-=upcnt
    if ans>=result:
        ans = result
        height = block
print(ans,height)