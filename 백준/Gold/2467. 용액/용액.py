n = int(input())
solution = list(map(int,input().split()))
start,end = 0, n-1
result = abs(solution[start] + solution[end])
left,right = start,end
while start<end:
    sumSolution = solution[start] + solution[end]
    if sumSolution == 0:
        left,right = start,end
        break
    if abs(sumSolution) < result:
        result = abs(sumSolution)
        left,right = start,end
    if sumSolution < 0: #용액의 합이 0 보다 작으면 왼쪽포인터이동
        start+=1
    elif sumSolution > 0: #용액의 합이 0보다 크면 오른쪽포인터이동
        end-=1
print(solution[left],solution[right])