from collections import defaultdict
xdict = defaultdict(int)
ydict = defaultdict(int)
for _ in range(3):
    a,b = map(int,input().split())
    xdict[a]+=1
    ydict[b]+=1
for x,y in xdict.items():
    if y==1:print(x,end=' ')
for x,y in ydict.items():
    if y==1:print(x)