from itertools import combinations
scb = [[]]+[list(input().split()) for _ in range(9)]
length = 0
check = dict()
for i in list(combinations(range(1,10),3)):
    s,c,b = set(),set(),set()
    for k in i:s.add(scb[k][0])
    for k in i:c.add(scb[k][1])
    for k in i:b.add(scb[k][2])
    if (len(s)==1 or len(s)==3) and (len(c)==1 or len(c)==3) and (len(b)==1 or len(b)==3):
        length+=1
        check[tuple(sorted(i))]=0

cnt = 0
result = 0
flag = 0
for _ in range(int(input())):
    s = input()
    if s.startswith('H'):
        tmp = tuple(sorted(list(map(int,list(s[1:].split())))))
        if tmp in check:
            if check[tmp]==0:
                result+=1
                check[tmp]+=1
                cnt+=1
            else:result-=1
        else:result-=1
    else:
        if not flag and length==cnt:
            result+=3
            flag = 1
        else:result-=1
print(result)