from collections import deque
input = __import__('sys').stdin.readline
n,m = map(int,input().split())
rail = [list(map(int,input().split())) for _ in range(n)]
count = [0 for _ in range(m+1)]
for i,j in rail:
    count[i]+=1
result = 0
rail = deque(rail)

def stack(data):
    total = data[0][1]
    tmp = [data[0][1]]
    for i in range(1,len(data)):
        tmp.sort(reverse=True)
        # sm+=data[i-1][1]
        if data[i][1]<=tmp[-1]:
            total+=data[i][1]
            tmp.append(data[i][1])
        else:
            sm = 0
            for k in tmp[::-1]:
                if k<data[i][1]:
                    sm+=k
                else:break
           
            total+=(sm*2)
            total+=data[i][1]
            tmp.append(data[i][1])
    return total

for i in range(m,0,-1):
    temp = []
    cnt = 0
    while True:
        if cnt==count[i]:
            result += stack(temp)
            break
        if rail[0][0]!=i:
            rail.append(rail.popleft())
            result+=rail[-1][1]
        elif rail[0][0]==i:
            temp.append(rail.popleft())
            cnt+=1
print(result)