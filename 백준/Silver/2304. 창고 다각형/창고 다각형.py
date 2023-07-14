n = int(input())
LH = sorted([list(map(int,input().split())) for _ in range(n)])
mxIdx = LH.index(max(LH,key=lambda x:x[1]))
temp = 0
result = 0
for i in range(1,mxIdx+1):
    if LH[temp][1] <= LH[i][1]:
        result += (LH[i][0]-LH[temp][0])*LH[temp][1]
        temp = i
temp = n-1
for i in range(n-2,mxIdx-1,-1):
    if LH[temp][1] <= LH[i][1]:
        result += (LH[temp][0]-LH[i][0])*LH[temp][1]
        temp = i
print(result+LH[mxIdx][1])