from collections import deque

def bfs():
    while queue:
        nowNum = queue.popleft()
        if nowNum =='123456789':
            return count[nowNum]
        idx = nowNum.find('9')
        x = idx//3
        y = idx%3
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=3 or ny>=3:continue
            nextIdx = 3*nx + ny
            nowlist = list(nowNum)
            nowlist[idx], nowlist[nextIdx] = nowlist[nextIdx], nowlist[idx]
            nextNum = ''.join(nowlist)
            if not count.get(nextNum):
                count[nextNum] = count[nowNum] + 1
                queue.append(nextNum)

dx,dy = [-1,1,0,0],[0,0,-1,1]

start = ""
for _ in range(3):
    temp = input()
    temp = temp.replace(" ","")
    start += temp
start = start.replace("0","9")

count = dict()
count[start] = 0

queue = deque()
queue.append(start)
result = bfs()
print(-1 if result == None else result)