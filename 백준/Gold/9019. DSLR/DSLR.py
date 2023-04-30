from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    q = deque([a])
    while q:
        x = q.popleft()
        for i in range(4):
            num= choose(i,x)
            if x==0 and i!=1:continue
            if 0<=num<10001 and check[num]=='':
                check[num] = check[x] + dslr[i]
                q.append(num)
    return check[b]


def choose(i,x):
    if i==0:
        return (x*2)%10000
    elif i==1:
        if x == 0:return 9999
        else: return x-1
    elif i==2:
        return x//1000 + (x%1000)*10
    else:
        return x//10 + (x%10)*1000


t = int(input())
dslr = ['D','S','L','R']
for _ in range(t):
    a,b = map(int,input().split())
    check = ['']*(10000+1)
    print(bfs(a,b))