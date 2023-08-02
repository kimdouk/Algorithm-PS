n,m = map(int,input().split())
graph = [input() for _ in range(n)]
temp = []
for i in range(n-7):
    for j in range(m-7):
        temp.append([row[j:j+8] for row in graph[i:i+8]])
mn = float('inf')
case1 = ['BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
case2 = ['WBWBWBWB','BWBWBWBW', 'WBWBWBWB' ,'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
for tmpgraph in temp:
    cnt1,cnt2 = 0,0
    for i in range(len(tmpgraph)):
        for j in range(len(tmpgraph[i])):
            if tmpgraph[i][j]!=case1[i][j]:cnt1+=1
            if tmpgraph[i][j]!=case2[i][j]:cnt2+=1
    mn = min(mn,cnt1,cnt2)
print(mn)