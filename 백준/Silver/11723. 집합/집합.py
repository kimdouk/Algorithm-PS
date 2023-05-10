#비트마스크
import sys
input = sys.stdin.readline
n = int(input())
s=0
for _ in range(n):
    data = list(input().split())
    if data[0]=='all':s = (1<<20)-1
    elif data[0]=='empty':s = 0
    else:
        num = int(data[1])-1
        if data[0] == 'add':s|= (1<<num)
        elif data[0]=='remove':s&= ~(1<<num)
        elif data[0]=='check':#우,,우와
            if s&(1<<num)==0:print(0)
            else:print(1)
        elif data[0]=='toggle':s^=(1<<num)