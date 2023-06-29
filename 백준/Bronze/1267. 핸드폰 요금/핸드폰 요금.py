n = int(input())
seconds = list(map(int,input().split()))
y,m = 0,0
for i in seconds:
    y+= 10+(i//30)*10
    m+= 15+(i//60)*15
if y<m:print('Y',y)
elif y>m:print('M',m)
else:print('Y','M',m)