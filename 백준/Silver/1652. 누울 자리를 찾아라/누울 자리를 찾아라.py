def search(line):
    cnt, result = 0,0
    for i in range(len(line)):
        if line[i]=='.':
            cnt+=1
        if cnt>=2 and line[i]=='X':
            result+=1
            cnt =0
        elif cnt>=2 and i==len(line)-1:
            result+=1
        elif cnt<2 and line[i]=='X':
            cnt = 0
    return result

n = int(input())
graph = [list(input()) for _ in range(n)]
row,col = 0,0
for i in graph:
    row+=search(i)
for j in range(n):
    col +=search([graph[i][j] for i in range(n)])
print(row,col)