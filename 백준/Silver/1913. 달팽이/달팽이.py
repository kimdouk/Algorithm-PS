n = int(input())
find = int(input())
x,y = n//2,n//2
num = 2
board = [[0]*n for _ in range(n)]
board[x][y] = 1
length = 0
dx = [0,1,0,-1]#우하좌상
dy = [1,0,-1,0]
while True:
  for i in range(4):
    for _ in range(length):
      nx = x +dx[i]
      ny = y +dy[i]
      board[nx][ny] = num
      num+=1
      x,y = nx,ny
  if x==0 and y==0:break
  length +=2
  x-=1
  y-=1
for i in range(n):
  if find in board[i]:
    a,b = i+1,board[i].index(find)+1
  print(*board[i])
print(a,b)