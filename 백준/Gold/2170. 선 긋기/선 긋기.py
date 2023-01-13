import sys
input = sys.stdin.readline

n = int(input())
lineList = [list(map(int,input().split())) for _ in range(n)]
lineList.sort() # 시작점이 빠른 순으로 정렬
startLine, endLine = lineList[0] #시작점이 제일 빠른 선부터 시작
result = 0

for i in range(1,len(lineList)): # 그 다음 선부터
    newStartLine, newEndLine = lineList[i] #다음 선은 new_
    if endLine >= newStartLine:#현재 끝점보다 새로운 시작점이 앞서있으면(끊어지지 않았으면)
        endLine = max(endLine,newEndLine) #((1,5)(2,4)를 생각하자)
    else:
        result += (endLine - startLine) #현재 끝점보다 새로운 시작점이 뒤에 있으면(끊어졌으면)
        startLine, endLine = newStartLine, newEndLine #새로운 시작점,끝점을 현재의 시작점,끝점으로 갱신
result += (endLine - startLine)#끊어졌든 안끊어졌든 마지막의 최장 선의 길이는 구해야 함.
print(result)