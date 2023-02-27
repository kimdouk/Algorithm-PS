from collections import deque
wheel = {}
for i in range(1,5):
    wheel[i] = deque(list(map(int,input())))
n = int(input())

def right(start, dirs):
    if start>4 or wheel[start][6] == wheel[start-1][2]:
        return
    if wheel[start][6] != wheel[start-1][2]:
        right(start+1,-dirs)
        wheel[start].rotate(dirs)

def left(start,dirs):
    if start< 1 or wheel[start+1][6] == wheel[start][2]:
        return
    if wheel[start+1][6] != wheel[start][2]:
        left(start-1, -dirs)
        wheel[start].rotate(dirs)

for _ in range(n):
    num, dirs = map(int,input().split())
    right(num+1,-dirs)
    left(num-1,-dirs)
    wheel[num].rotate(dirs)

total = 0
for i in range(1,5):
    if wheel[i][0]==1:
        total += (2**(i-1))
print(total)