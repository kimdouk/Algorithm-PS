import sys
input = sys.stdin.readline
n,m = map(int,input().split())
x,y,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
move = [(-1,0),(0,1),(1,0),(0,-1)] #북동남서
visited = [[False for _ in range(m)] for _ in range(n)]
result = 1
visited[x][y] = True
def back(x,y,d):
    global result
    nx = x + move[(d+2)%4][0]
    ny = y + move[(d+2)%4][1]
    if graph[nx][ny]==1:
        print(result)
        sys.exit()
    elif graph[nx][ny]==0 and not visited[nx][ny]:
        result +=1
        visited[nx][ny] = True
        return nx, ny
    else:return nx, ny

def rotate(d):
    nd = (d+3)%4
    return nd

def clean(x,y,d):
    global result
    nx = x+move[d][0]
    ny = y+move[d][1]
    if graph[nx][ny]==0 and not visited[nx][ny]:
        result+=1
        visited[nx][ny] = True
        x,y = nx,ny
        return x,y,True
    return x,y,False


while True:
    goback = 1
    for i in range(4):
        d = rotate(d)
        x,y,flag= clean(x,y,d)
        if flag:
            goback=0
            break
    if goback:
        x,y = back(x,y,d)
print(result)