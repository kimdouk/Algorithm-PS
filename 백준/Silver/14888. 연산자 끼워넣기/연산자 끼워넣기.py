from itertools import permutations
n = int(input())
numbers = list(map(int,input().split()))
arr = list(map(int,input().split()))
operatorList = []
for i in range(1,len(arr)+1):
    for j in range(arr[i-1]):
        operatorList.append(i)
answer = [0] * n
answer[0] = numbers[0]
result = []
for operators in list(permutations(operatorList,len(operatorList))):
    for i in range(len(operators)):
        if operators[i] ==1:
            answer[i+1] = answer[i] + numbers[i+1]
        elif operators[i] ==2:
            answer[i+1] = answer[i] - numbers[i+1]
        elif operators[i] ==3:
            answer[i+1] = answer[i] * numbers[i+1]
        elif operators[i] ==4:
            if answer[i] <0 and numbers[i+1]>0:
                answer[i+1] = -(abs(answer[i]) // numbers[i+1])
            else: answer[i+1] = answer[i] // numbers[i+1]
    result.append(answer[-1])
print(max(result), min(result),sep='\n')