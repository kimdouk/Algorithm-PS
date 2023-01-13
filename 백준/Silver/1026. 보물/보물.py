n = int(input())
listA = sorted(list(map(int,input().split())))
listB = list(map(int,input().split()))
result = 0

for i in range(n):
    num = listB.pop(listB.index(max(listB)))
    result += (listA[i]*num)
print(result)