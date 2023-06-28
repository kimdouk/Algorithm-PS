import sys

def rotated(arr):
    # a = zip(*arr[::-1])
    # return [*map(list,a)]
    n = len(arr)
    m = len(arr[0])
    new = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-1-i] = arr[i][j]
    return new

def isAttach(i,j,sticker):
    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if sticker[x][y]==1 and notebook[x+i][y+j]==1:
                return False
    return True

def attach(i,j,sticker):
    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if sticker[x][y] ==1:
                notebook[x+i][y+j]=1

input = sys.stdin.readline
n,m,k = map(int,input().split())
notebook = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    cnt=0
    flag = 0
    while cnt<4:
        if flag==1:break
        for i in range(n-len(sticker)+1):
            if flag==1:break
            for j in range(m-len(sticker[0])+1):
                if isAttach(i,j,sticker):
                    attach(i,j,sticker)
                    flag = 1
                    break
        sticker = rotated(sticker)
        cnt+=1

result = 0
for i in notebook:
    result+=i.count(1)
print(result)